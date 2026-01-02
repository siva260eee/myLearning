# Device Financing Agentic AI - Learning Guide

## 📚 Table of Contents
1. [Introduction to Agentic AI](#introduction-to-agentic-ai)
2. [Understanding Device Financing](#understanding-device-financing)
3. [Agent Architecture](#agent-architecture)
4. [Decision-Making Process](#decision-making-process)
5. [Training Your Agent](#training-your-agent)
6. [Hands-On Exercises](#hands-on-exercises)
7. [Advanced Topics](#advanced-topics)

---

## 1. Introduction to Agentic AI

### What is Agentic AI?

Agentic AI refers to autonomous artificial intelligence systems that can:
- **Make decisions independently** based on learned patterns
- **Adapt to new situations** without explicit programming
- **Explain their reasoning** for transparency
- **Learn from experience** to improve over time
- **Balance multiple objectives** simultaneously

### Why Device Financing?

Device financing is an excellent domain for learning Agentic AI because:
- **Multiple factors to consider**: Credit score, income, preferences, market conditions
- **Clear success metrics**: Customer satisfaction, default rates, profitability
- **Real-world complexity**: Risk assessment, regulatory compliance
- **Transparent decisions**: Customers need explanations for recommendations

---

## 2. Understanding Device Financing

### Key Concepts

#### Credit Score
- **Excellent (740+)**: Best rates, 0% APR options available
- **Good (670-739)**: Competitive rates, most options available
- **Fair (580-669)**: Higher rates, limited options
- **Poor (<580)**: Very limited options, may need cosigner

#### Interest Rate (APR)
- **0% APR**: No interest, total cost = device price
- **5-10% APR**: Low interest, typical for good credit
- **10-20% APR**: Higher interest, typical for fair/poor credit

#### Monthly Payment Affordability
- **Ideal**: < 10% of monthly income
- **Acceptable**: 10-15% of monthly income
- **Risky**: > 15% of monthly income

#### Term Length
- **Short (6-12 months)**: Higher monthly payment, lower total cost
- **Medium (18-24 months)**: Balanced approach
- **Long (36+ months)**: Lower monthly payment, higher total cost

### The 8 Training Cases

| Case | Device | Customer Type | Credit Score | Key Challenge |
|------|--------|---------------|--------------|---------------|
| 1 | iPhone 15 Pro Max | High Income | 780 | Choosing best 0% APR option |
| 2 | Galaxy S24 | Average Income | 650 | Balancing affordability with existing loans |
| 3 | iPad Pro (10x) | Corporate | 800 | Bulk purchase, business needs |
| 4 | Pixel 7a | Limited Income | 580 | Working with credit constraints |
| 5 | Gaming Laptop | Student | 620 | Utilizing cosigner benefits |
| 6 | Apple Watch Ultra | Loyal Customer | 720 | Rewarding customer loyalty |
| 7 | Fire HD 10 | Senior | 750 | Simplicity over optimization |
| 8 | MacBook Pro | Freelancer | 690 | Variable income considerations |

---

## 3. Agent Architecture

### Core Components

```typescript
DeviceFinancingAgent
├── Configuration
│   ├── agentId: string
│   ├── modelType: 'rule-based' | 'ml-based' | 'hybrid'
│   ├── decisionThreshold: number
│   └── weights: DecisionWeights
├── Decision Logic
│   ├── filterQualifyingOptions()
│   ├── scoreFinancingOption()
│   ├── buildDecision()
│   └── createNoQualificationDecision()
├── Training & Evaluation
│   ├── train()
│   ├── evaluate()
│   └── getPerformanceMetrics()
└── State Management
    ├── exportState()
    ├── updateConfig()
    └── logDecision()
```

### Decision Weights Explained

```typescript
weights: {
    totalCostWeight: 0.25,         // How much to prioritize low total cost
    monthlyPaymentWeight: 0.30,     // How much to prioritize affordable payments
    customerPreferenceWeight: 0.20, // How much to honor customer's term preference
    creditScoreWeight: 0.15,        // How much to factor in credit optimization
    termLengthWeight: 0.10          // How much to consider term length impact
}
```

**Weight Examples:**
- **Conservative Agent**: High totalCostWeight (0.40), minimize long-term cost
- **Affordability Agent**: High monthlyPaymentWeight (0.45), minimize monthly burden
- **Customer-First Agent**: High customerPreferenceWeight (0.35), honor preferences

---

## 4. Decision-Making Process

### Step-by-Step Workflow

#### Step 1: Qualification Filtering
```typescript
// Only consider options where creditScore >= creditScoreRequired
const qualifyingOptions = options.filter(
    opt => customer.creditScore >= opt.creditScoreRequired
);
```

#### Step 2: Multi-Factor Scoring

For each option, calculate scores across multiple dimensions:

**A. Total Cost Efficiency (0-100 points)**
```typescript
costScore = (1 - (totalCost - basePrice) / basePrice) * 100
// Example: 0% APR option gets 100, 10% APR option might get 85
```

**B. Monthly Payment Affordability (0-100 points)**
```typescript
paymentRatio = monthlyPayment / monthlyIncome
if (paymentRatio < 0.10) affordabilityScore = 100
else if (paymentRatio < 0.15) affordabilityScore = 80
else if (paymentRatio < 0.20) affordabilityScore = 60
else affordabilityScore = 40
```

**C. Term Preference Match (0-100 points)**
```typescript
termPreferenceScore = 100 - abs(months - preferredPeriod) * 5
// Example: Perfect match = 100, 6 months off = 70
```

**D. Interest Rate Score (0-100 points)**
```typescript
interestScore = (1 - interestRate) * 100
// Example: 0% = 100, 5% = 95, 10% = 90
```

**E. Early Payoff Penalty Bonus (+20 points)**
```typescript
penaltyBonus = earlyPayoffPenalty ? 0 : 20
```

**Final Score**
```typescript
totalScore = (costScore * 0.25) + 
             (affordabilityScore * 0.30) + 
             (termPreferenceScore * 0.20) + 
             (interestScore * 0.15) + 
             (penaltyBonus * 0.10)
```

#### Step 3: Ranking & Selection
- Sort all options by totalScore (descending)
- Select highest-scoring option as recommendation
- Keep next 2 options as alternatives

#### Step 4: Risk Assessment
```typescript
// Identify potential risks
- High payment-to-income ratio (> 15%)
- Multiple existing device loans
- Low credit score (< 650)
- Long-term commitment with variable income
```

#### Step 5: Confidence Calculation
```typescript
confidence = min(95, max(60, topOption.score))
// Higher score = higher confidence
// Capped at 95% (never 100% certain)
```

---

## 5. Training Your Agent

### Training Process

```typescript
// 1. Load all cases
const allCases = getDeviceFinancingCases(); // 8 cases

// 2. Split data
const trainingSet = allCases.slice(0, 6);  // 75% for training
const testSet = allCases.slice(6);         // 25% for testing

// 3. Train agent
agent.train(trainingSet);
// Agent analyzes each case and compares its recommendation 
// with the labeled "optimal" choice

// 4. Evaluate on test set
const metrics = agent.evaluate(testSet);

// 5. Review results
console.log(`Accuracy: ${metrics.accuracy}%`);
console.log(`Avg Confidence: ${metrics.averageConfidence}%`);
```

### Improving Agent Performance

**If accuracy is low (<70%):**
1. Adjust decision weights to match labeled optimal choices
2. Review cases where agent disagrees with optimal choice
3. Consider if "optimal" labels need refinement

**If confidence is low (<75%):**
1. Increase weight on factors with clear advantages
2. Add more discriminating factors to scoring
3. Refine risk assessment logic

**If decisions vary too much:**
1. Increase decisionThreshold for more consistent choices
2. Reduce weight variance (make weights more similar)

---

## 6. Hands-On Exercises

### Exercise 1: Analyze a Single Case (Beginner)

**Objective**: Understand basic agent usage

```typescript
import { DeviceFinancingAgent } from './src/agents';
import { getFinancingCaseById } from './src/device_financing/cases';

// TODO: Create an agent with default configuration
const agent = new DeviceFinancingAgent({
    // Fill in configuration
});

// TODO: Get case #1 (premium smartphone)
const case1 = getFinancingCaseById(1);

// TODO: Analyze the case
const decision = agent.analyzeFinancingCase(case1);

// TODO: Print the recommendation and reasoning
console.log(decision);
```

**Questions to Answer:**
1. What option was recommended?
2. What was the confidence level?
3. What were the top 3 reasoning factors?
4. Were any risk factors identified?

---

### Exercise 2: Compare Agent Strategies (Intermediate)

**Objective**: Understand how weights affect decisions

```typescript
// TODO: Create three agents with different strategies
const conservative = new DeviceFinancingAgent({
    weights: {
        totalCostWeight: 0.40,      // Minimize cost
        monthlyPaymentWeight: 0.20,
        // ... complete the rest
    }
});

const affordability = new DeviceFinancingAgent({
    weights: {
        totalCostWeight: 0.15,
        monthlyPaymentWeight: 0.45,  // Minimize payment
        // ... complete the rest
    }
});

const balanced = new DeviceFinancingAgent({
    weights: {
        // ... all weights equal
    }
});

// TODO: Test all three on case #2 (mid-range smartphone)
// TODO: Compare recommendations
```

**Questions to Answer:**
1. Did all agents recommend the same option?
2. Which agent prioritized total cost savings?
3. Which agent prioritized monthly affordability?
4. In what scenarios would each strategy be best?

---

### Exercise 3: Train and Evaluate (Intermediate)

**Objective**: Learn the training process

```typescript
// TODO: Create an agent
const agent = new DeviceFinancingAgent({ /* config */ });

// TODO: Get all cases and split into train/test
const allCases = getDeviceFinancingCases();
// Split: cases 1-6 for training, 7-8 for testing

// TODO: Train the agent
agent.train(trainingCases);

// TODO: Evaluate on test set
const metrics = agent.evaluate(testCases);

// TODO: Print detailed results
```

**Questions to Answer:**
1. What was the training accuracy?
2. What was the test accuracy?
3. Which cases did the agent get wrong?
4. Why might there be a difference between training and test accuracy?

---

### Exercise 4: Create a Custom Case (Advanced)

**Objective**: Design your own financing scenario

```typescript
// TODO: Create a custom financing case
const customCase = {
    id: 100,
    caseTitle: "Your Scenario Here",
    device: {
        deviceType: "Smartwatch",  // Your choice
        brand: "Garmin",
        model: "Fenix 7",
        basePrice: 699,
        msrp: 699
    },
    customer: {
        customerId: "CUSTOM-001",
        creditScore: 680,  // Your choice
        monthlyIncome: 4200,  // Your choice
        existingDeviceLoans: 1
    },
    // TODO: Add 3 financing options
    financingOptions: [
        // Option 1: 12-month 0% APR
        // Option 2: 24-month 6% APR
        // Option 3: 36-month 9% APR
    ],
    marketContext: { /* ... */ },
    agentDecisionFactors: [ /* ... */ ]
};

// TODO: Analyze with agent
// TODO: Manually determine optimal choice
// TODO: Compare agent's decision with yours
```

**Questions to Answer:**
1. What option did you expect the agent to choose?
2. Did the agent agree with your choice?
3. If not, what factor caused the difference?
4. How would changing weights affect the decision?

---

### Exercise 5: Implement Custom Scoring (Advanced)

**Objective**: Extend the agent with new decision factors

```typescript
// TODO: Modify the agent to add a "credit building" factor
// Idea: Prefer options that help customer build credit
//   - Shorter terms = faster payoff = better for credit
//   - On-time payments = credit boost
//   - Low utilization = credit boost

// TODO: Add creditBuildingWeight to DecisionWeights

// TODO: Calculate creditBuildingScore in scoreFinancingOption()
// Consider:
//   - Term length (shorter is better for credit)
//   - Payment history potential
//   - Credit utilization impact

// TODO: Incorporate into final score calculation

// TODO: Test on low-credit cases (case #4)
```

---

## 7. Advanced Topics

### Machine Learning Integration

**Supervised Learning Approach:**

```typescript
// 1. Export training data
const trainingData = exportTrainingData();

// 2. Train ML model (using TensorFlow.js, PyTorch, etc.)
const model = trainModel(trainingData);

// 3. Use ML predictions in agent
class MLBasedAgent extends DeviceFinancingAgent {
    scoreFinancingOption(option, customer, device) {
        // Use ML model to predict score
        return model.predict(option, customer, device);
    }
}
```

### Real-Time Market Data

**Integrate live market conditions:**

```typescript
interface MarketData {
    currentInterestRates: number[];
    competitorPromotions: Promotion[];
    deviceDemand: number;
    inventoryLevels: Map<string, number>;
}

// Update agent to consider real-time data
const decision = agent.analyzeFinancingCase(
    financingCase,
    marketData  // Live market context
);
```

### Multi-Agent Systems

**Coordinate multiple specialized agents:**

```typescript
const riskAssessmentAgent = new RiskAgent();
const pricingAgent = new PricingAgent();
const recommendationAgent = new RecommendationAgent();

// Ensemble decision
const riskScore = riskAssessmentAgent.assess(customer);
const pricingScore = pricingAgent.score(options);
const recommendation = recommendationAgent.decide(
    options, 
    riskScore, 
    pricingScore
);
```

### Reinforcement Learning

**Learn from customer feedback:**

```typescript
// Track customer outcomes
interface Outcome {
    caseId: number;
    recommendedOption: string;
    customerAccepted: boolean;
    paymentSuccess: boolean;
    customerSatisfaction: number;
}

// Update agent based on feedback
agent.updateFromFeedback(outcomes);
```

---

## 📖 Additional Resources

### Books
- "Artificial Intelligence: A Modern Approach" by Russell & Norvig
- "Hands-On Machine Learning" by Aurélien Géron

### Online Courses
- Coursera: AI for Everyone
- Fast.ai: Practical Deep Learning

### Related Projects
- LangChain: Building agents with LLMs
- AutoGPT: Autonomous AI agents
- Microsoft Semantic Kernel: Agentic AI framework

---

## ✅ Learning Checklist

- [ ] Understand what Agentic AI is
- [ ] Know all 8 device financing cases
- [ ] Create and configure an agent
- [ ] Analyze a single case
- [ ] Compare different agent strategies
- [ ] Train an agent on multiple cases
- [ ] Evaluate agent performance
- [ ] Interpret accuracy and confidence metrics
- [ ] Design custom financing scenarios
- [ ] Implement custom scoring logic
- [ ] Integrate ML models (optional)
- [ ] Build multi-agent systems (optional)

---

**Ready to build intelligent financing agents? Start with Exercise 1!** 🚀
