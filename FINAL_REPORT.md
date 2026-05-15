# DealFlowBench-mini: PE/VC Investment Agent Benchmark

## 1. 摘要

本项目选择 **PE/VC 投资经理 / 投资分析师** 作为目标岗位，构建一个面向长程高价值投资工作流的 Agent Benchmark：**DealFlowBench-mini**。

该 benchmark 不评估模型是否会回答金融知识题，而是评估 Agent 是否能在接近真实投资工作环境的 workspace 中，完成以下链路：

```text
ambiguous partner request
-> read multi-file data room
-> verify operating / financial metrics
-> identify management narrative vs raw-data tension
-> form investment judgment
-> produce team-ready artifacts
```

本次 mini prototype 构建了 3 个 synthetic-but-realistic data rooms，覆盖 VC / Growth / PE 三类投资场景，并实现了一个轻量自动化评估 harness。实测覆盖 DeepSeek、Kimi、Gemini、Doubao 等模型，输出了 task-level score matrix 和 failure-mode analysis。

核心发现：

- 主流模型普遍能完成 memo、KPI check、risk log、follow-up email 等 artifacts。
- 模型对关键事实和投资风险的覆盖能力较强。
- 真正拉开差距的是 **细分 KPI / spreadsheet discipline**：例如 cohort retention、channel economics、monetization conversion、working capital schedule。
- Eval 系统需要区分 model-quality failure 和 provider/runtime/harness failure，例如 Gemini 503、Kimi 初始 thinking-mode 空 content、长任务 remote disconnection。

## 2. 岗位选择与真实工作流

目标岗位：**PE/VC 投资经理 / 投资分析师**

选择该岗位的原因：

- 任务具有高经济价值，直接影响投资决策。
- 工作天然跨文档、表格、邮件、模板、会议材料等多种应用。
- 投资判断依赖长上下文、多源证据、计算核验和反证识别。
- 输出不是单句答案，而是能进入真实 deal team workflow 的 artifacts。

典型工作场景拆解：

| 工作场景 | 真实需求 | Agent 能力要求 |
|---|---|---|
| Deal screening | 判断新项目是否值得推进 | 多文件阅读、商业判断、风险识别 |
| KPI sanity check | 核验管理层指标是否可靠 | 表格计算、口径识别、异常检测 |
| Market / competitive review | 判断增长和差异化是否可持续 | 市场理解、替代品分析、动态更新 |
| Financial diligence | 验证收入质量、毛利、现金流和营运资本 | 财务表解析、bridge 分析、working capital 判断 |
| IC preparation | 产出投资委员会可用材料 | memo、risk log、follow-up email、template following |

## 3. Benchmark 任务设计

DealFlowBench-mini 包含 3 个代表性任务。每个任务都不是孤立问答，而是模拟投资经理收到一个 partner request 后，在 data room 中完成初筛、核验、判断和交付物产出的过程。

| Task | 标的 | 投资类型 | 核心问题 | 主要能力 |
|---|---|---|---|---|
| T001 | HomePal Robotics | VC / Series A | AI 家庭机器人是否有真实家庭需求，还是只有 demo 兴奋？ | cohort retention、commercial intent、hardware margin、manufacturing risk |
| T002 | StoryForge AI | VC / Seed-A | AI 漫剧生产效率是否转化为可持续内容商业优势？ | content economics、paid conversion、platform dependency、IP risk |
| T003 | VoltBridge Mobility | PE / Growth | e-bike 出海增长是否高质量，还是被库存/渠道/现金流风险掩盖？ | revenue quality、gross margin、AR aging、inventory、cash conversion、regulatory risk |

### 3.1 T001：HomePal Robotics

**标的定位与产品内容**

HomePal Robotics 是一家虚构的 AI 家庭机器人公司，产品是面向家庭场景的 AI companion robot。它覆盖三个使用场景：老人照护提醒、儿童互动、家庭助手。产品形态结合语音交互、视觉识别、轻量移动、家庭日程提醒和 household memory。

**投资语境**

该公司处在 **Series A** 阶段，融资诉求是 $18M。语境偏 **VC**，核心不是看利润，而是判断早期 PMF、使用留存、商业化意愿、硬件毛利和量产风险是否足以支撑继续推进。

**任务**

Agent 需要阅读 data room，完成：

- `product_kpi_check.csv`：核验用户留存、预购、订阅意愿、硬件毛利、warranty、制造良率等指标。
- `investment_memo.md`：输出 preliminary investment memo。
- `risk_log.md`：列出关键风险。
- `founder_follow_up_email.md`：写给创始人的追问邮件。

**Data room 特点与代表性张力**

这组 data room 的核心张力是：**管理层把一个局部成立的老人照护场景，包装成整体家庭机器人 PMF。**

- 管理层强调 core care cohort 30 日留存 72%，但全体 pilot household 口径明显更低。
- 老人照护场景有真实需求，儿童互动有强 demo 效果但留存下降、安全投诉更多。
- 家庭助手场景容易被智能音箱和手机 app 替代。
- 预购和订金存在，但 gross preorder 需要扣除 cancellation，渠道质量差异很大。
- 管理层量产毛利乐观，但 pilot cost、warranty reserve 和 manufacturing yield 暴露硬件商业化风险。

这道题主要考 Agent 能不能区分 **demo excitement** 和 **durable household demand**。

### 3.2 T002：StoryForge AI

**标的定位与产品内容**

StoryForge AI 是一家虚构的 AI-native 内容工作室，生产短篇漫剧、AI 生成漫画和竖屏连续剧。它通过 TikTok、YouTube Shorts、Reels、Webtoon-style 平台和自有 app 分发内容。

**投资语境**

该公司处在 **Seed-A / pre-Series A** 阶段，语境偏 **VC**。核心问题不是它能不能用 AI 降本，而是 AI workflow 是否真的带来可持续内容商业优势。

**任务**

Agent 需要阅读 production workflow、episode performance、cost comparison、platform distribution、copyright/IP memo、audience comments 等材料，完成：

- `content_kpi_check.csv`：核验单集成本、制作周期、完播率、续看率、付费转化、平台集中度。
- `investment_memo.md`：判断是否继续推进。
- `risk_log.md`：列出内容、平台、版权、付费风险。
- `founder_follow_up_email.md`：写给创始人的追问邮件。

**Data room 特点与代表性张力**

这组 data room 的核心张力是：**AI 生产效率是真实的，但不自动等于内容/IP 生意成立。**

- AI 把单集成本从 $6,800 降到 $2,450，制作周期从 14 天缩短到 4.5 天。
- 但产量提升不等于爆款可复制，也不等于付费转化强。
- views 和 paid users 集中在少数头部 series。
- TikTok 是主要流量来源，平台算法变化会影响新剧曝光。
- audience comments 暴露剧情套路、角色脸漂、结尾弱、AI-looking 等质量问题。
- copyright/IP memo 暴露 asset provenance 和 chain-of-title 不完善，影响长期 IP licensing。

这道题主要考 Agent 能不能避免 **output-volume bias**：不能因为 AI 产量提高，就直接判断公司有投资价值。

### 3.3 T003：VoltBridge Mobility

**标的定位与产品内容**

VoltBridge Mobility 是一家虚构的 e-bike 出海品牌，拥有中国供应链背景，面向欧洲和东南亚销售 urban commuter、folding e-bike、cargo e-bike 和低价入门车型。渠道包括欧洲经销商、Amazon marketplace、DTC site 和东南亚零售伙伴。

**投资语境**

该公司处在 **Growth / PE** 阶段，融资诉求是 $20M growth capital。语境偏 **PE/growth**，核心不是早期 PMF，而是判断收入增长质量、毛利、库存、应收账款、现金流和合规风险是否支持投资。

**任务**

Agent 需要阅读 management presentation、三大表、adjusted EBITDA bridge、working capital schedule、AR aging、inventory aging、warranty returns、regulatory memo 等材料，完成：

- `operating_kpi_check.csv`：核验收入增长、ASP、毛利、EBITDA、经营现金流、库存天数、AR aging、CCC、warranty cost。
- `ic_investment_note.md`：输出 IC-style investment note。
- `risk_log.md`：列出经营质量和财务风险。
- `management_follow_up_email.md`：写给管理层的追问邮件。

**Data room 特点与代表性张力**

这组 data room 的核心张力是：**收入增长是真的，但增长质量和现金流质量并不好。**

- 2025 年收入增长 51%，但 blended ASP 下滑，低毛利渠道占比提升。
- 管理层展示正的 adjusted EBITDA，但 reported EBITDA 和 operating cash flow 为负。
- adjusted EBITDA bridge 中有较多低质量 add-back，例如 launch marketing、incremental warranty、inventory markdown。
- AR aging 显示 top distributors 应收集中且账龄拉长。
- inventory aging 显示欧洲老库存压力。
- warranty and returns 显示电池和 motor controller claims 上升。
- regulatory memo 显示欧盟 EN15194、电池运输和合规文件仍有缺口。

这道题主要考 Agent 能不能从 **headline growth** 进入 **operating diligence**，而不是只复述管理层的增长故事。

## 4. Data room 构建与迭代

本项目使用 **synthetic-but-realistic data rooms**，而非直接使用上市公司公开材料。

原因：

- 保证任务可控、可复现、可自动评分。
- 避免训练集污染和网页动态变化。
- 避免真实公司/客户数据保密问题。
- 允许有意识地设计管理层叙事与底层数据之间的 tension。

数据结构参考真实 PE/VC 尽调材料，包括：

- partner request email
- management presentation / company overview
- operating metrics
- financial pack
- customer / audience / distributor notes
- legal / regulatory / IP memo
- competitor / market snapshot
- memo or IC note template

Data room 不是一次写完的。每个 task 都经历了“看起来像题目”到“更像真实投资材料”的调整。

| 任务 | 第一版的问题 | 具体改动 | 为什么这样改 |
|---|---|---|---|
| T001 | 最早只有一个汇总 usage table，Agent 很容易直接读 total，任务像产品分析题，不像投资尽调。 | 把 `pilot_usage_metrics.csv` 改成 cohort-level 表，按城市、场景、获客渠道拆分 D1/D7/D14/D30 retention、complaint tickets、safety tickets、return intent。 | 真实 VC 不会只看一个平均留存，而会追问哪个场景留存好、哪个渠道质量差、管理层有没有选择性披露。 |
| T001 | 早期硬件公司只有 usage 还不够。用户喜欢 demo，不代表愿意付钱。 | 增加 `commercialization_metrics.csv`，包含 gross preorders、deposit、cancelled preorders、net preorders、CAC、subscription trial opt-in、paid pilot households。 | Series A 公司可以没有完整三表，但至少要有早期商业化证据。这样 Agent 必须判断使用行为和付费意愿是否一致。 |
| T001 | 家庭机器人这个标的容易被“AI demo 很酷”带偏。 | 增加 `bom_and_margin_table.csv` 和 `manufacturing_plan.md`，埋入 pilot cost、warranty reserve、first-pass yield、battery certification、tooling delay。 | 硬件 AI 项目的真实风险不只在 PMF，也在毛利、售后、量产和认证。 |
| T002 | 第一版如果只写 AI workflow 降本，Agent 很容易给出“成本下降，所以值得看”的浅层结论。 | 增加 `episode_performance.csv`，按 series 拆 views、starts、completions、continuations、engaged viewers、paid users、revenue。 | 内容公司不能只看产量，要看完播、续看、付费和头部集中度。 |
| T002 | AI 内容长期价值取决于平台和 IP，但这两块在第一版不够明显。 | 增加 `platform_distribution_report.md` 和 `copyright_ip_memo.md`。 | 这样 Agent 需要识别 TikTok dependency、algorithm risk、asset provenance、style similarity、chain-of-title 等真实投资风险。 |
| T002 | 纯数字表不能解释内容质量为什么不稳定。 | 增加 `audience_comments.md`，放入用户对套路剧情、角色脸漂、AI-looking、结尾弱的反馈。 | 投资经理会把数据和用户反馈交叉验证，而不是只看播放量。 |
| T003 | 第一版偏运营表，像 export business review，不够像 PE data room。 | 增加 `income_statement.csv`、`balance_sheet.csv`、`cash_flow_statement.csv`。 | Growth / PE 任务需要看利润、现金流、资产负债表，不然不能判断经营质量。 |
| T003 | 简化三表仍然不够，无法测试 adjusted EBITDA 质量。 | 增加 `adjusted_ebitda_bridge.csv`，把 reported EBITDA 调到 management adjusted EBITDA，并标出 add-back 质量。 | PE 尽调经常要判断 add-back 是否真实 non-recurring。这里可以测试 Agent 是否会挑战管理层 EBITDA。 |
| T003 | 只看 inventory aging 还不够，现金转换压力没有展开。 | 增加 `working_capital_schedule.csv` 和 `ar_aging.csv`。 | 这样 Agent 可以核验 DSO、DIO、DPO、CCC，并发现大客户应收逾期、返利争议和保修扣款。 |

## 5. 自动化评估设计

本项目的自动化评估不是让另一个模型随便打分，而是把 task 拆成几类可验证对象：交付物、数值计算、关键事实、必要风险、正向信号和 failure mode。

### 5.1 Ground truth 是什么

每个 task 的 ground truth 分成三层：

| Ground truth 类型 | 内容 | 例子 |
|---|---|---|
| 数值型 ground truth | 从 data room 中可复算的指标，写入 `calculation_checks.json` | T001 全体 30 日留存 46.9%；T002 paid conversion 9.3%；T003 CCC 126.7 天 |
| 事实型 ground truth | 强答案必须覆盖的关键事实，写入 `golden_facts.json` | T001 老人照护强、儿童互动投诉高；T002 TikTok 占 71% views；T003 adjusted EBITDA add-back 质量差 |
| 风险型 ground truth | 投资判断中必须识别的风险，写入 `must_identify_risks` | warranty reserve 低估、IP provenance 不足、AR aging 恶化 |

这些 ground truth 不是唯一答案，而是“强投资分析至少应该覆盖的证据点”。

### 5.2 Verifier 是什么

Verifier 是自动检查器，用来判断模型输出是否满足 task 要求。它不是完整的人类投资专家，而是一个可重复执行的初筛评分器。

| Verifier | 检查对象 | 检查方式 | 作用 |
|---|---|---|---|
| Artifact verifier | 模型是否生成指定文件 | 检查 run 目录中是否存在 required artifacts | 判断模型是否完成工作流，而不是只写一段回答 |
| Calculation verifier | 模型是否写出关键数值 | 在输出中匹配 expected value / expected display | 检查 KPI workpaper 是否完整 |
| Golden fact verifier | 模型是否覆盖关键事实 | 对 golden facts 做关键词/短语覆盖匹配 | 检查模型是否读到 data room 的核心证据 |
| Risk verifier | 模型是否识别必要风险 | 对 must-identify risks 做覆盖匹配 | 检查投资判断是否抓住关键风险 |
| Positive signal verifier | 模型是否识别正向信号 | 对 expected positive signals 做覆盖匹配 | 避免模型只会唱衰，要求平衡判断 |
| Failure tagger | 模型触发了哪些能力缺口 | 根据缺失项打 failure tags | 用于定位能力边界，而不只是给总分 |

### 5.3 怎么 eval

每次模型运行后，系统读取模型生成的 artifacts，并按以下顺序评分：

```text
artifact presence
-> calculation coverage
-> golden fact coverage
-> required risk coverage
-> positive signal coverage
-> failure tag assignment
-> score report
```

本次自动总分采用加权组合：

| 评分项 | 权重 | 理由 |
|---|---:|---|
| Artifact completion | 20% | 投资 Agent 必须能产出可交付文件 |
| Calculation coverage | 30% | 金融工作中数字核验是关键能力，也是最可验证部分 |
| Golden fact coverage | 25% | 检查模型是否真正读懂 data room |
| Required risk coverage | 20% | 检查投资判断是否抓住关键风险 |
| Positive signal coverage | 5% | 防止模型只列风险、不识别投资亮点 |

这个 evaluator 的目标不是替代人类 IC 判断，而是先自动筛出三类问题：

1. 模型有没有完成工作流。
2. 模型有没有算对关键指标。
3. 模型有没有覆盖关键证据和风险。

### 5.4 当前边界

当前 verifier 仍然是轻量版：

- 数字检查主要看 expected value 是否出现在输出中，还没有完整解析模型生成的 CSV。
- golden fact coverage 是关键词级匹配，可能对好的 paraphrase 低估，也可能对堆关键词的回答高估。
- memo 的投资逻辑质量还没有接入 calibrated LLM judge 或 PE/VC 专家人工评分。

因此，当前分数更适合作为 **自动化初筛分数**，不是最终投资判断质量的绝对排名。

## 6. 模型设置

本次测试使用以下模型：

| Provider | Model | 说明 |
|---|---|---|
| DeepSeek | `deepseek-v4-flash` | 成本友好的 flash baseline |
| Moonshot / Kimi | `kimi-k2.6` | 与目标岗位高度相关；测试中处理了 thinking-mode API 行为 |
| Gemini | `gemini-2.5-flash` | 国际 flash baseline；T002/T003 遇到 provider-side availability errors |
| Doubao | `doubao-seed-1-6-flash-250828` | 国内大厂 flash baseline |

统一设置：

- 同一 task prompt。
- 同一 data room。
- 不使用外部网页搜索。
- 要求输出相同 artifacts。
- 使用同一 evaluator。

## 7. 实测结果

最新 score matrix 如下：

| Task | Model | Total | Artifacts | Calculations | Golden Facts | Risks | Failure Tags |
|---|---|---:|---:|---:|---:|---:|---|
| T001 | DeepSeek v4 Flash | 86.36 | 100.00 | 54.55 | 100.00 | 100.00 | `retention_miss`, `margin_miscalculation` |
| T001 | Doubao Seed 1.6 Flash | 87.73 | 100.00 | 59.09 | 100.00 | 100.00 | `retention_miss`, `margin_miscalculation` |
| T001 | Gemini 2.5 Flash | 90.45 | 100.00 | 68.18 | 100.00 | 100.00 | - |
| T001 | Kimi k2.6 | 91.82 | 100.00 | 72.73 | 100.00 | 100.00 | - |
| T002 | DeepSeek v4 Flash | 90.00 | 100.00 | 66.67 | 100.00 | 100.00 | - |
| T002 | Doubao Seed 1.6 Flash | 95.00 | 100.00 | 83.33 | 100.00 | 100.00 | - |
| T002 | Kimi k2.6 | 85.00 | 100.00 | 50.00 | 100.00 | 100.00 | `monetization_miss` |
| T003 | DeepSeek v4 Flash | 86.25 | 100.00 | 54.17 | 100.00 | 100.00 | `asp_decline_miss`, `margin_mix_miss`, `inventory_miss` |
| T003 | Doubao Seed 1.6 Flash | 87.50 | 100.00 | 58.33 | 100.00 | 100.00 | `asp_decline_miss`, `margin_mix_miss`, `inventory_miss` |
| T003 | Kimi k2.6 | 88.75 | 100.00 | 62.50 | 100.00 | 100.00 | - |

结果文件：

- `results/eval_matrix.csv`
- `results/failure_matrix.md`
- `results/run_failure_log.md`
- `results/harness_iteration_log.md`

## 8. 结果解读

### 8.1 成功 run 的 artifact completion 普遍很强

所有成功 run 都产出了 required artifacts。这说明在 task schema 清楚的情况下，当前主流模型可以完成专业工作流里的基本交付物格式要求。

### 8.2 模型普遍擅长高层投资综合

Golden fact 和 required-risk 分数整体较高。模型普遍能识别主要 diligence issue：

- T001：留存口径混用、儿童安全投诉、硬件毛利压力、量产风险。
- T002：平台依赖、付费转化弱、头部剧集集中、IP provenance 风险。
- T003：ASP 下滑、毛利压力、经营现金流为负、AR 和 inventory 同时膨胀、监管风险。

### 8.3 主要差距来自 spreadsheet discipline

模型之间最大的差异出现在 calculation checks。很多模型能理解投资故事，但没有完整填出所有 segment / channel / financial calculations。

具体例子：

- T001：部分模型漏掉 child / family segment retention、complaint rate 或 warranty reserve 计算。
- T002：Kimi 漏掉部分 monetization conversion checks。
- T003：DeepSeek 和 Doubao 对 ASP decline、margin mix、inventory / working capital checks 展开不完整。

这是投资 Agent 的一个重要能力边界：**定性知道结论不够，junior investment professional 还必须产出完整 workpapers。**

### 8.4 Provider/runtime failure 需要和模型能力失败分开

测试过程中出现过几类运行层问题：

- Kimi k2.6 在初始 non-streaming thinking-mode 调用下返回空 content。
- Gemini 在 T002/T003 遇到 provider-side high demand / connection errors。
- 部分长上下文任务需要提高 timeout 才能稳定完成。

这些失败被单独记录，并从模型能力评分中排除。这一点很重要：真实 eval system 不能把 API availability、连接稳定性、harness compatibility 和模型任务能力混在一起。

## 9. 定性展示

为了避免只看自动分数，本节抽取部分模型输出，用中文概括其表现。这里不是完整人工评分，而是展示 evaluator 分数背后的实际回答质量。

### 9.1 较好样例：Kimi 在 T001 中的投资判断

Kimi 对 HomePal Robotics 的建议是 **Hold**。其核心判断可以概括为：

> 老人照护场景显示出真实 PMF，但制造准备度、硬件毛利、儿童互动安全/留存、订阅商业化都还没有充分验证，因此不应直接 lead $18M Series A。

它进一步指出：

- 老人照护的 day-30 retention、subscription interest 和 family notification 需求最强。
- 儿童互动有 week-one excitement，但 30 天后留存下降，且 open-ended chat 有安全与投诉问题。
- 家庭助手场景被智能音箱和 app 替代的风险高。
- 管理层的 72% retention 是选择性口径，不能代表整体家庭场景 PMF。
- pilot cost 下硬件毛利只有约 20.5%，warranty reserve 也被低估。

这个样例说明 Kimi 不只是复述 data room，而是能把 product usage、commercial intent、hardware economics 和 manufacturing risk 合成一个投资建议。

### 9.2 较好样例：DeepSeek 在 T003 中的 PE-style 判断

DeepSeek 对 VoltBridge Mobility 的建议是 **Request Revised Plan**。其核心判断可以概括为：

> 收入增长是真的，但增长质量差；ASP 下滑、毛利下降、库存和应收吃现金、warranty cost 上升，管理层 adjusted EBITDA 不能掩盖 reported EBITDA 和 operating cash flow 的压力。

它明确提到：

- top 3 欧洲经销商占总收入 51.5%，并且有账期、返利争议和 warranty claim。
- operating cash flow 为 -$9.8M，增长依赖外部融资。
- CCC 明显高于管理层口径。
- 19% 库存超过 180 天，欧洲老库存更严重。
- 监管和电池运输成本没有充分进入经营计划。

这个样例说明模型可以完成较复杂的 PE operating diligence，但自动评分仍然扣了 calculation 分，因为部分细分指标没有全部写进 KPI 表。

### 9.3 较弱样例：Kimi 在 T002 中的 monetization workpaper 不完整

Kimi 在 T002 的 memo 中能识别 StoryForge AI 的主要风险，例如平台依赖、IP 风险和内容质量问题；但在 `content_kpi_check.csv` 中，对 monetization 的细分计算不够完整。

例如，它能写出：

- cost per episode 从 $6,800 降到 $2,450。
- production cycle 从 14 天降到 4.5 天。
- paid conversion among engaged viewers 约 9.27%，低于管理层 11%。

但它对 revenue per completed viewer、completion denominator、platform-level monetization 的处理不够稳定。因此 evaluator 标记了 `monetization_miss`。

这个样例说明：模型可能在 memo 中讲对大方向，但在 KPI workpaper 中漏掉关键计算。对于真实投资工作，这会影响 analyst 输出的可审计性。

## 10. Failure mode 分析

最常见的 failure modes：

| Failure Mode | 含义 | 观察到的模式 |
|---|---|---|
| `retention_miss` | 缺少细分 retention / cohort checks | T001 中 DeepSeek 和 Doubao 抓住了结论，但没有完整列出细分 cohort 计算 |
| `margin_miscalculation` | 毛利、warranty 或 margin bridge 写得不完整 | T001 中 DeepSeek 和 Doubao |
| `monetization_miss` | 付费转化、收入质量、viewer monetization 细节不完整 | T002 中 Kimi |
| `asp_decline_miss` | 没有充分展开 ASP 下滑 | T003 中 DeepSeek 和 Doubao |
| `margin_mix_miss` | 没有充分展开 channel / region margin deterioration | T003 中 DeepSeek 和 Doubao |
| `inventory_miss` | 没有充分展开库存老化或 working capital pressure | T003 中 DeepSeek 和 Doubao |

综合来看，模型不是“不懂业务”，而是经常没有把底层数据完全转成结构化 workpaper。未来的 investment-agent benchmark 不应该只看 memo 写得像不像投资人，还应该重视 spreadsheet / tool-use precision。

## 11. 局限性

当前局限：

- Data rooms 是 synthetic 的，虽然结构和张力参考真实 PE/VC 材料，但仍需要从业者校准。
- Golden fact coverage 目前是关键词级匹配，可能低估好的 paraphrase，也可能高估堆关键词的回答。
- Calculation checks 目前检查 expected values 是否出现，还没有完整解析模型生成的 CSV。
- Memo 质量还没有接入 calibrated LLM judge 或 PE/VC expert review。
- 当前只有 3 个 seed tasks，还不是大规模 benchmark suite。
- 部分 provider availability 影响了 run 稳定性，目前只是记录和排除，还没有完整 retry policy。

## 12. 后续迭代

建议后续迭代：

1. 从 3 个任务扩展到 20-50 个 synthetic data rooms，覆盖更多行业、阶段和任务类型。
2. 对模型生成的 CSV artifacts 做结构化解析，而不是只做 expected value 匹配。
3. 增加 LLM-as-judge，用固定 rubric 评估 memo 质量、投资判断和表达专业度。
4. 用小样本 PE/VC expert review 校准自动评分。
5. 加入 browser、file system、spreadsheet trace scoring，评估真正跨应用 Agent。
6. 生成 randomized task variants，降低过拟合和 prompt leakage。
7. 增加 provider retry policy 和 run-stability metrics。

## 13. 结论

DealFlowBench-mini 展示了一种评估 PE/VC investment agents 的可落地方法：把模型放进真实感 workspace，而不是考金融问答。

这个 benchmark 要求模型阅读多源材料、核验指标、识别管理层叙事和底层数据的矛盾、形成投资建议，并输出专业 artifacts。

初步结果显示，当前模型已经很擅长 synthesis 和 risk identification，但在完整 KPI workpaper 和细分财务/运营计算上仍有明显差异。这正是 Agent benchmark 应该暴露的能力边界：不是模型能不能“像投资人一样说话”，而是它能不能完成真实投资团队依赖的跨文档、跨表格、可审计工作。
