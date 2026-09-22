# DR-M02 — Harness Design Principles

> Status: **preview v0.16.8**> Creator / Lead Author: **riottt**

## 6.0 Why Harness Engineering Emerged

Harness Engineering was not invented one day as a single Tool technique.
Each time the work delegated to AI expanded, one more problem outside the Prompt was solved. Following that accumulation makes the current shape easier to understand.

This is not a strict "single official chronology" but a **DeepRail technology-history model** connecting published product history and technical articles with practical design changes.

### 6.0.1 Stage 1 — Prompt Engineering: Shaping AI Output

The initial concern was how to ask AI to obtain the desired answers and code.

```text
Human
  ↓
Prompt / Instruction / Example / Output Format
  ↓
Model
  ↓
Output
```

The central question here is **"how to phrase things to get better output."**
Prompt Engineering is still necessary, but once AI becomes a Worker executing multiple Steps, the Prompt alone is not enough as a design target.

### 6.0.2 Stage 2 — Persistent Rules / Repository Context: Not Repeating the Same Things

Once AI IDEs entered practice, users naturally wanted the following.

- Follow these conventions every time in this Repository
- Do not make me explain this Project's structure and Domain every time
- Always use this assumption for this File / Directory
- Do not repeat the same cautions every Session

```text
Explain in a Prompt every time
        ↓
Persistent Rule / Repository Context
        ↓
Continuously steer Project-specific behavior
```

Rather than product names, we want to see the change that happened here.
**Instead of restating things in a Prompt every time, people wanted to leave assumptions on the environment side.** That demand widened the design target slightly outward.

### 6.0.3 Stage 3 — Context Engineering: Designing the AI's State of Awareness

When an Agent handles long work, what matters more than writing Instructions is **what it knows at the moment it reasons**.

The difference is easy to see this way.

```text
Prompt Engineering
"How to say it"

Context Engineering
"What state of knowledge it works with"
```

Context candidates include Requirements, Code, Architecture, Domain Knowledge, Decisions, Environment State, Tool Descriptions, History, and more.
**The goal is not to put more into Context, but to pass the right information, sufficiently, at the right moment.**

### 6.0.4 Stage 4 — Coding Agent: AI from Answering to Acting

Once AI reads and writes Files, runs the Terminal, Tests, and Retries, the user's questions change.

```text
What to make it answer
        ↓
How far to let it act
What to forbid
What to verify automatically
Where to return on failure
When to escalate to a Human
```

At this stage, not only Rules / Context but **Tools, Permissions, Feedback, Retry, and Gates** become necessary.

### 6.0.5 Stage 5 — Harness Engineering: Integrating Guardrails and Enablement into the Execution System

Harness Engineering is not a technology for merely restraining AI.
In practice, two desires arise simultaneously.

```text
CONTROL / GUARDRAIL
├ Prohibitions
├ Permission
├ Hook / Gate
├ CI
├ Human Approval
└ Audit / Evidence

ENABLEMENT
├ Context
├ Source of Truth
├ Skill
├ Tool / MCP
├ Environment
├ Memory / Artifact
├ Retry / Recovery
└ Evaluation / Feedback
```

The definition in DeepRail:

> **Harness Engineering is the engineering of an execution system — covering not only Prompt / Context but also Tool, Permission, SCM, CI/CD, Environment, Gate, Eval, Evidence, Recovery, Human Decision, and Learning — so that AI can complete work safely and reproducibly.**

### 6.0.6 Closer to Spontaneous Emergence than "Invention"

Before the name took hold, similar countermeasures were already emerging in the field.

If you repeat the same caution many times, you want to make it a Rule. If a dangerous operation scares you, you want to narrow Permissions. If "it's done" alone feels unreliable, you want Tests and Evidence.

Here we only note that this flow is not accidental. **Where delegating work causes trouble, the necessary mechanism is born.**

In the next Why, we use FlowDesk to follow that emergence inside a single job. How to let people experience the same flow in education is left to the talent development chapter.

### 6.0.6.1 Why — Why Does Harness Engineering Emerge Spontaneously?

You do not need to build the completed form of a Harness from the start.

Rather, in many cases, you delegate work first. Then you hit problems. Mechanisms are born where the problems are.

Suppose FlowDesk's proxy approval was initially delegated as-is to a single Agent. You ask it to "implement this request and pass the Tests." The Agent reads the Repository, writes Code, and adds Tests. For a small change, that might be all it takes.

But widen the work a little and the same approach breaks down.

You explain what "proxy" means every time. You explain the audit Log Rule every time. You warn every time about Production Data that must not be touched. Every time a Test fails, a human teaches the cause. Every time the Agent says "it's done," a human verifies by other means. When the Session changes, the previous cautions disappear.

Around here, the field starts adding countermeasures even without knowing the names.

```text
Don't want to repeat the same explanation
→ Rule / Context

Want it to read the necessary Sources without getting lost
→ Source of Truth / Retrieval

Want to stop dangerous operations
→ Permission / Hook

"It's done" alone is not enough to decide
→ Test / Evidence / Eval

Don't want humans fixing it every time it fails
→ Feedback / Retry / Recovery

Don't want to repeat the same Failure next time
→ Reinvestment
```

Add these one by one, and before you know it, you have "an execution environment that makes work for AI hold together."

A Harness is not necessarily a special device built from a completed blueprint. As the scope of delegated work widens, missing conditions become visible, and it often appears as the result of filling those gaps.

That is why starting from Tools tends to get the order wrong. If you decide the Agent Framework and Skill list first, parts accumulate without knowing which Failures they prevent or which work they exist to make possible.

Conversely, starting from the work reveals the necessity.

You want to delegate proxy approval safely in FlowDesk. Then: which information is needed? How far may it operate? By what is correctness judged? Where does it return on failure? Which decisions should be asked of a human? What is left for next time?

Answer these questions one by one, and Context, Permission, Verification, Gate, Decision, and Learning connect.

This is also why the Harness is derived backward from the Delivery System. What we want to build is not a flashy AI feature. **It is the conditions under which work holds together to the end.**

If the scope delegated to AI is narrow, the Harness is small. As the scope widens, the design target expands outward.

> **If you pursue delegation seriously, you need mechanisms that make work hold together. Harness Engineering is what makes those mechanisms reproducible rather than leaving them as accidental ingenuity.**

### 6.0.7 The Design Target Expands Outward

Looking at the flow of technology, earlier ways of thinking do not disappear; rather, the design target expands outside them.

```text
Prompt Engineering
Design instructions to AI
        ↓
Context Engineering
Design the AI's state of awareness
        ↓
Harness Engineering
Design the AI's actions, environment, verification, and recovery
        ↓
Operating Model / Organization Engineering
Design the roles, authority, decision-making, and learning of Human + AI
```

Neither Prompt Engineering nor Context Engineering disappears.
**They remain as important design areas inside Harness Engineering.**

Also, when generalizing Harness Engineering to organizations, do not map Software's mechanical Gates directly onto humans; verify the conditions under which they hold and abstract them.

### 6.0.8 Structural Similarity Between Strong Organizations and Strong Harnesses

A strong company does not stand on excellent individuals alone. By translating Purpose, Principles, Roles, Authority, Processes, Evaluation, and Learning into lower-level behavior, it aligns individual judgment and raises reproducibility and autonomy.

The same problem appears in a Harness.

| Organization | Harness / AI Execution System |
|---|---|
| Purpose / Mission | Intent / Objective |
| Values / Principles | Instructions / Rules |
| Organizational Knowledge | Context / Source of Truth |
| Role | Agent / Function |
| Authority | Permission |
| Business Process | Workflow / Skill |
| Approval / Internal Control | Gate / Human Decision |
| Performance / Quality Evaluation | Eval / Evidence |
| Audit / Monitoring | Observability / Trace |
| Training / Organizational Learning | Reinvestment / Rule / Skill Update |

This similarity is not for equating AI with humans.
**It shows that when multiple execution agents are moved autonomously and reproducibly toward a purpose, the design problems that arise are similar.**

### 6.0.8.1 Why — Why Do Similar Structures Appear in Organizations and Harnesses?

We do not intend to describe a company and an AI Harness as the same thing.

People have emotions, relationships, and legal responsibility, and organizations have culture and power. DeepRail does not take the simple metaphor that an organization can be designed by treating an Agent as an employee.

Still, put the blueprints side by side and similar things appear. Purpose. Roles. Authority. Flow of work. Decision criteria. Exception handling. Evaluation. Audit. Learning.

The reason they look similar is not that humans and AI are alike. **You delegate work to multiple execution agents and want the whole to move toward the purpose without the center instructing every single item.** That problem is shared.

In a small company, the president can decide every detail and it still runs, because the president is the Context, the Gate, and the Evaluator. As headcount grows, that stops working. You share what you aim for, decide who may decide what, push routine work into Processes, and raise only significant exceptions.

The same happens in AI Execution. While there is one Agent and a human sits beside it watching everything, Prompts and conversation alone can run. As Agents multiply, work lengthens, and it starts spanning multiple Repositories and Environments, humans can no longer directly control every Step.

What is needed then is Intent, Context, Role, Permission, Workflow, Gate, Evidence, Escalation, and Reinvestment.

This is not a claim to "treat AI as an employee."

> **When multiple execution agents can move toward a purpose without constant human intervention, organizations and Harnesses approach the same kind of design problem.**

With this view, a Harness can no longer be treated as mere Developer Tooling. Permitting an Agent to perform Production operations does not end with Tool Permission. It becomes a Decision Rights problem: based on whose policy, up to which Risk Class, and with which Evidence can that judgment be delegated downward.

Conversely, on the Organization side, saying "introduce AI Tools" is not enough either. Where does Strategy turn into Work, what passes to AI, and what returns as Evidence to higher-level judgment? Unless that much is designed, management Intent and AI Execution do not connect.

It was the same in FlowDesk. What an Agent implementing proxy approval needs is not only Code Conventions. Who is allowed proxy approval, what is kept for audit, which exceptions return to a human. If that higher-level Rule does not reach Execution, technically correct Code can still be wrong as a Business.

A strong Harness is not a mechanism that makes AI look smart. A strong Organization is not a state of merely gathering excellent people. Both have **a structure that delivers purpose to lower-level action and returns the Evidence of action to higher-level learning**.

Follow Harness Engineering deep enough and you return to the story of Organization. Rather than having stretched the topic, the expansion of work delegated to AI made visible a problem that was connected from the start.

### 6.0.9 Connecting Management Intent to AI Execution

The higher the abstraction of the work AI takes on, the less Coding Rules alone suffice.

```text
Coding Standard
↓
Engineering Principle
↓
Product Principle
↓
Risk Appetite
↓
Business Priority
↓
Decision Policy
↓
Strategy / Purpose
```

Do not stuff all of these into a Prompt.
Clarify the Source of Truth and Decision Rights of each layer, and build a structure where necessary Intent reaches lower-level Execution and lower-level Evidence returns to higher-level Decision.

```text
Purpose / Strategy
↓
Objective / Portfolio Decision
↓
Operating Model / Decision Policy
↓
Work Contract / Harness
↓
AI / Human Execution
↓
Evidence / Outcome / Failure
↑
Management Review / Organizational Learning
↑
Strategy Update
```

At this point, Harness Engineering is no longer mere Developer Tooling; it becomes **a lower layer that makes Organization Engineering executable**.

---

## 6.1 Harness Design Starts from Understanding the Delivery System

Harness design does not start from runtime-specific Instruction Files, Prompts, Agent Personas, or Skill lists.

First, draw **how the team's changes are made, verified, approved, delivered to production, and rolled back on failure**.

```text
Demand / Requirement
↓
Specification
↓
Work Item
↓
Source Change
↓
Build
↓
Static Check
↓
Unit / Integration / E2E
↓
Security / Compliance Check
↓
Artifact
↓
Review / Approval
↓
Deploy
↓
Production Verification
↓
Monitoring
↓
Rollback / Incident
↓
Learning
```

If you design a Harness without understanding this Flow, you can write "what to have AI do" but cannot design the following.

- Where to stop AI
- Which verification to leave to machines
- What to accept as Evidence to proceed
- Which permissions can be handed to which Agent
- Where Human Decision is needed
- How to separate Environment Failure from Implementation Failure
- How far Release / Rollback can be autonomized
- How to return failures to Rules / Skills / Evals

**CI/CD is not an integration target attached behind the Harness. It is the Delivery Backbone to look at before designing the Harness.**

---

## 6.2 The 14 Items to Confirm First at Design Time

| Item | Question |
|---|---|
| Outcome | What is this Harness meant to make hold together |
| Development Lifecycle | From requirements to Learning, by which responsibilities and Gates does it proceed |
| SCM / Work Isolation | What are the units of change and of parallel work |
| CI/CD | Where do Build / Test / Package / Deploy run, and triggered by what |
| Test / Eval | What can machines verify, and what do humans judge |
| Environment | How are Local / Shared / CI / Staging / Production states distinguished |
| Release / Rollback | What are the conditions for production release and recovery |
| Work Unit | What are the units: Epic / Feature / Issue / Agent Task / PR, etc. |
| Source of Truth | What is the canonical source for requirements, specifications, Code, Decisions |
| Human Gate | Where is human judgment required |
| Agent Boundary | Where is the scope delegated to AI and the forbidden scope |
| Evidence | By what are progress and completion proven |
| External Tool | How to integrate with Issue / Chat / Docs / Cloud etc. |
| Runtime / Model | Which Agent Runtime / Model is used, and is it replaceable |

---

## 6.3 Create a Control Point Map

For each point in the Delivery Flow, record the following.

```text
Control Point
├ Trigger
├ Actor: Human / AI / Machine
├ Input
├ Allowed Action
├ Required Evidence
├ Pass Condition
├ Failure Route
├ Escalation Owner
├ Permission Boundary
└ Traceability Target
```

Example:

| Control Point | Actor | Evidence | On Failure | Harness Implementation Candidates |
|---|---|---|---|---|
| Before Implementation | AI + Human as needed | Spec / Acceptance / Decision | Return to Align / Specify | Skill / Decision Packet |
| Pre-commit | Machine / AI | Lint / unit test | Agent retry | Hook |
| PR/MR | AI + Human | Review Packet / CI result | Rework / Decision | Review Skill / Gate |
| Integration | CI | Integration result / env provenance | Environment or Code route | CI Gate / Env checker |
| Release | Human / Policy | Release Decision Packet | Defer / Fix | Approval Gate |
| Production | CD + Runtime | Deployment / smoke / monitoring | Rollback / Incident | Tool / Runbook / Agent |

**The Harness makes this Control Point Map executable.**

---

## 6.4 "Map, not Encyclopedia"

Do not write all information in the Harness entry file.

The recommended philosophy:

```text
Short entry point
├── Links to the current Development / Delivery Flow
├── Links to canonical documents
├── Build/Test/CI commands
├── How to identify Environments
├── Prohibitions / Permission Boundary
└── Skills/Agents to call when needed
```

Deep content is loaded when it becomes necessary.

This aims to:

- Avoid constant injection of unnecessary Context
- Separate rule responsibilities
- Make update locations easy to identify
- Separate CI/CD and Environment facts from Prompt-level assumptions
- Make the AI Runtime easier to replace

---

## 6.5 The Harness Is "Scaffolding" and Changes with Model Capability

Each Harness component implicitly holds an assumption about "what the Model alone cannot do."
Because that assumption ages as the Model evolves, do not keep the Harness fixed while it grows complex.

Principles:

1. Fix the Control Objective required on Delivery first.
2. Adopt the minimum Harness that satisfies that Control Objective.
3. Record the reason each Rule / Skill / Agent / Hook was added.
4. When the Model updates, Eval whether the added scaffolding is still needed.
5. If Outcome / Evidence / Safety can be maintained after removal, simplify.


---

## 6.6 Harness Maturity

Give the Harness itself a maturity model.

| Level | State |
|---|---|
| H0 | Centered on individual Prompts |
| H1 | Common Instructions exist |
| H2 | Rules/Skills/Agents are role-separated |
| H3 | Connected to SCM / CI/CD / External Tools / Quality Gates |
| H4 | Changes are evaluated by Evals |
| H5 | Autonomous execution per Issue/Feature |
| H6 | Integrated management of multiple Agents and Work Items, with traceability through Delivery |

Harness maturity and AI autonomy level are not the same.
Even with an advanced Harness, keep the Human Gate for high-risk work.
