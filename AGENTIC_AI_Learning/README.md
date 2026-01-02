# AGENTIC AI Learning - Device Financing Intelligence

A comprehensive framework for building, training, and deploying intelligent AI agents specialized in device financing decision-making. This project demonstrates practical applications of agentic AI in financial services, focusing on optimal financing recommendation systems.

## 🎯 Project Overview

AGENTIC AI Learning provides a complete ecosystem for:
- **Intelligent Decision Making**: AI agents that analyze customer profiles and financing options to make optimal recommendations
- **Real-World Scenarios**: 8+ detailed device financing cases covering smartphones, tablets, laptops, and smartwatches
- **Agent Training**: Comprehensive training and evaluation framework for improving agent performance
- **Multi-Strategy Agents**: Different agent configurations (conservative, affordability-focused, balanced) for various business needs

## 📚 Learning Objectives

This project teaches you:
1. **Agentic AI Fundamentals**: How to design autonomous decision-making agents
2. **Multi-Factor Decision Making**: Balancing customer needs, financial constraints, and business objectives
3. **Agent Training & Evaluation**: Measuring and improving AI agent performance
4. **Real-World Application**: Applying AI to practical business problems (device financing)
5. **TypeScript AI Development**: Building production-ready AI systems with type safety

## 🏗️ Project Structure

```
AGENTIC_AI_Learning/
├── src/
│   ├── agents/
│   │   └── index.ts                 # Core AI agent implementation
│   ├── device_financing/
│   │   └── cases.ts                 # 8 comprehensive financing scenarios
│   ├── examples/
│   │   └── agent_demo.ts            # 6 demo scenarios showcasing agent capabilities
│   ├── tests/
│   │   └── agent.test.ts            # Comprehensive test suite
│   ├── types/
│   │   └── index.ts                 # TypeScript type definitions
│   └── app.ts                       # Express API server
├── package.json
├── tsconfig.json
└── README.md
```

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
cd AGENTIC_AI_Learning

# Install dependencies
npm install

# Build TypeScript files
npm run build

# Run the application
npm start
```

### Run Demos

```bash
# Run all demos to see agent capabilities
ts-node src/examples/agent_demo.ts
```

### Run Tests

```bash
# Execute test suite
npm test
```

## 💡 Key Features

### 1. Comprehensive Device Financing Cases

8 real-world scenarios covering:
- **Premium Smartphone** (Excellent Credit) - iPhone 15 Pro Max financing
- **Mid-Range Smartphone** (Average Credit with Trade-In) - Samsung Galaxy S24
- **Business Tablet Purchase** (Corporate Account) - Bulk iPad Pro purchase
- **Budget Smartphone** (Credit-Challenged) - Google Pixel 7a
- **Gaming Laptop** (Student with Cosigner) - ASUS ROG Strix G16
- **Smartwatch Upgrade** (Loyal Customer) - Apple Watch Ultra 2
- **Budget Tablet** (Senior First-Time Buyer) - Amazon Fire HD 10
- **Premium Laptop** (Freelancer Business) - MacBook Pro 16-inch

Each case includes:
- Detailed device specifications and pricing
- Customer credit profile and income data
- 3+ financing options with varying terms
- Market context and competitive landscape
- Optimal recommendation with reasoning

### 2. Intelligent Agent System

The `DeviceFinancingAgent` class provides:

```typescript
// Create an agent
const agent = new DeviceFinancingAgent({
    agentId: 'agent-001',
    name: 'FinancingExpert',
    modelType: 'hybrid',
    decisionThreshold: 0.75,
    weights: {
        totalCostWeight: 0.25,
        monthlyPaymentWeight: 0.30,
        customerPreferenceWeight: 0.20,
        creditScoreWeight: 0.15,
        termLengthWeight: 0.10
    }
});

// Analyze a case
const decision = agent.analyzeFinancingCase(financingCase);

// Train the agent
agent.train(trainingCases);

// Evaluate performance
const metrics = agent.evaluate(testCases);
```

**Agent Capabilities:**
- ✅ Multi-factor decision analysis (cost, affordability, preferences, credit)
- ✅ Risk assessment and mitigation
- ✅ Confidence scoring
- ✅ Alternative recommendation
- ✅ Training and continuous improvement
- ✅ Performance tracking and metrics

### 3. Decision-Making Process

The agent follows a sophisticated workflow:

1. **Qualification Check**: Filters options based on customer credit score
2. **Multi-Factor Scoring**: Evaluates each option across 5+ dimensions
3. **Risk Analysis**: Identifies potential payment challenges
4. **Reasoning Generation**: Provides transparent decision rationale
5. **Alternative Suggestions**: Recommends backup options
6. **Confidence Assessment**: Quantifies decision certainty

### 4. Training & Evaluation

```typescript
// Split data for training and testing
const allCases = getDeviceFinancingCases();
const trainSet = allCases.slice(0, 6);
const testSet = allCases.slice(6);

// Train the agent
agent.train(trainSet);

// Evaluate performance
const metrics = agent.evaluate(testSet);
// Output: accuracy, confidence, decision logs
```

## 📖 Detailed Examples

### Example 1: Basic Agent Usage

```typescript
import { DeviceFinancingAgent } from './agents';
import { getFinancingCaseById } from './device_financing/cases';

// Create agent
const agent = new DeviceFinancingAgent({
    agentId: 'basic-001',
    name: 'BasicAgent',
    modelType: 'rule-based',
    decisionThreshold: 0.7
});

// Analyze premium smartphone case
const premiumCase = getFinancingCaseById(1);
const decision = agent.analyzeFinancingCase(premiumCase);

console.log('Recommendation:', decision.recommendedOptionId);
console.log('Confidence:', decision.confidence);
console.log('Reasoning:', decision.reasoning);
```

### Example 2: Agent Comparison

```typescript
// Create agents with different strategies
const conservativeAgent = new DeviceFinancingAgent({
    weights: {
        totalCostWeight: 0.40,  // Minimize total cost
        monthlyPaymentWeight: 0.25,
        // ...
    }
});

const affordabilityAgent = new DeviceFinancingAgent({
    weights: {
        totalCostWeight: 0.15,
        monthlyPaymentWeight: 0.45,  // Minimize monthly payment
        // ...
    }
});

// Compare recommendations
const testCase = getFinancingCaseById(2);
const decision1 = conservativeAgent.analyzeFinancingCase(testCase);
const decision2 = affordabilityAgent.analyzeFinancingCase(testCase);
```

### Example 3: Category Analysis

```typescript
import { getFinancingCasesByDeviceType } from './device_financing/cases';

// Analyze all smartphone cases
const smartphoneCases = getFinancingCasesByDeviceType('Smartphone');
smartphoneCases.forEach(case => {
    const decision = agent.analyzeFinancingCase(case);
    console.log(`${case.caseTitle}: ${decision.recommendedOptionId}`);
});
```

## 🧪 Testing

Comprehensive test suite covering:
- Agent initialization and configuration
- Case analysis accuracy
- Credit score handling
- Affordability calculations
- Risk factor identification
- Training and evaluation
- Edge cases and error handling

Run tests:
```bash
npm test
```

## 📊 API Endpoints

The Express server provides REST endpoints:

```
GET /api/device-financing-cases
    Returns all financing cases

GET /api/device-financing-cases/:id
    Returns specific case by ID

POST /api/analyze-case
    Analyzes a case and returns agent recommendation
    Body: { caseId: number, agentConfig: AgentConfig }

GET /api/cases/device-type/:type
    Returns cases filtered by device type

GET /api/cases/credit-score/:min/:max
    Returns cases within credit score range
```

## 🎓 Learning Path

### Beginner Level
1. Run `demo1_BasicAgentUsage()` to understand agent basics
2. Explore [cases.ts](src/device_financing/cases.ts) to see case structure
3. Review [types/index.ts](src/types/index.ts) for data models

### Intermediate Level
4. Run `demo2_TrainingAgent()` to learn about agent training
5. Experiment with different agent weights in `demo6_AgentComparison()`
6. Study decision-making logic in [agents/index.ts](src/agents/index.ts)

### Advanced Level
7. Implement custom scoring algorithms
8. Add new device categories and financing scenarios
9. Create ML-based agent implementations
10. Build a UI for the recommendation system

## 🔧 Customization

### Add New Financing Cases

Edit [src/device_financing/cases.ts](src/device_financing/cases.ts):

```typescript
{
    id: 9,
    caseTitle: "Your New Case",
    device: {
        deviceType: "Smartphone",
        brand: "BrandName",
        model: "ModelName",
        basePrice: 999,
        msrp: 999
    },
    customer: {
        customerId: "CUST-009",
        creditScore: 700,
        monthlyIncome: 4000,
        existingDeviceLoans: 0
    },
    // ... add financing options and other fields
}
```

### Customize Agent Weights

Adjust decision priorities:

```typescript
const agent = new DeviceFinancingAgent({
    weights: {
        totalCostWeight: 0.30,      // Higher = prefer lower total cost
        monthlyPaymentWeight: 0.35,  // Higher = prefer lower monthly payment
        customerPreferenceWeight: 0.20,
        creditScoreWeight: 0.10,
        termLengthWeight: 0.05
    }
});
```

## 🎯 Use Cases

This framework can be adapted for:
- **Device Financing**: Smartphones, tablets, laptops (current implementation)
- **Auto Loans**: Vehicle financing recommendations
- **Personal Loans**: Unsecured loan optimization
- **Mortgage Lending**: Home loan analysis
- **Credit Card Selection**: Optimal credit card recommendations
- **Insurance Products**: Policy recommendation engines

## 📈 Performance Metrics

Agent performance is measured across:
- **Accuracy**: % of recommendations matching optimal choices
- **Confidence**: Average confidence in decisions
- **Training Time**: Time to train on dataset
- **Decision Logs**: Complete history of all decisions

Example output:
```
📊 Evaluation Results:
   Accuracy: 87.50%
   Correct: 7/8
   Avg Confidence: 84.23%
```

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Additional device categories (e.g., home appliances)
- Machine learning model integration
- Enhanced risk assessment algorithms
- UI/UX frontend implementation
- Multi-language support
- Real-time market data integration

## 📄 License

This project is licensed under the MIT License.

## 🔗 Related Resources

- **Agentic AI Concepts**: Learn about autonomous agents
- **TypeScript Best Practices**: Type-safe AI development
- **Financial Decision Systems**: Credit scoring, risk assessment
- **Machine Learning**: Supervised learning for recommendations

## 📧 Support

For questions or issues, please open a GitHub issue or contact the maintainers.

---

**Built with ❤️ for learning Agentic AI and practical financial applications**