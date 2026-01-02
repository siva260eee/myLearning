# Quick Start Guide - Device Financing Agentic AI

Get up and running with device financing AI agents in 5 minutes!

## ⚡ Quick Installation

```bash
cd AGENTIC_AI_Learning
npm install
npm run build
```

## 🎯 Run Your First Demo

```bash
# Run all demos to see agent capabilities
npm run demo
```

This will run 6 interactive demos showing:
1. Basic agent usage
2. Agent training process
3. Category-based analysis
4. Credit score filtering
5. Training data export
6. Agent strategy comparison

## 🚀 Start the API Server

```bash
npm start
```

Visit: http://localhost:3000/api/docs for API documentation

## 📊 Try These Quick Examples

### Example 1: Analyze Premium Smartphone Case

```bash
# Using curl or Postman
curl http://localhost:3000/api/analyze-case \
  -H "Content-Type: application/json" \
  -d '{"caseId": 1}'
```

**Expected Output:**
- Recommended financing option
- Confidence score
- Detailed reasoning
- Risk factors
- Alternative options

### Example 2: Get All Smartphone Cases

```bash
curl http://localhost:3000/api/cases/device-type/Smartphone
```

### Example 3: Filter by Credit Score

```bash
# Get cases for customers with 700-800 credit score
curl http://localhost:3000/api/cases/credit-score/700/800
```

### Example 4: Train an Agent

```bash
curl http://localhost:3000/api/train-agent \
  -H "Content-Type: application/json" \
  -d '{
    "trainingCaseIds": [1, 2, 3, 4, 5, 6],
    "testCaseIds": [7, 8]
  }'
```

## 💻 Code Examples

### Create and Use an Agent

```typescript
import { DeviceFinancingAgent } from './src/agents';
import { getFinancingCaseById } from './src/device_financing/cases';

// Create agent
const agent = new DeviceFinancingAgent({
    agentId: 'my-agent',
    name: 'MyFirstAgent',
    modelType: 'rule-based',
    decisionThreshold: 0.7,
    weights: {
        totalCostWeight: 0.25,
        monthlyPaymentWeight: 0.30,
        customerPreferenceWeight: 0.20,
        creditScoreWeight: 0.15,
        termLengthWeight: 0.10
    }
});

// Analyze a case
const case1 = getFinancingCaseById(1);
const decision = agent.analyzeFinancingCase(case1);

console.log('Recommendation:', decision.recommendedOptionId);
console.log('Confidence:', decision.confidence + '%');
console.log('Reasoning:', decision.reasoning);
```

### Train an Agent

```typescript
import { getDeviceFinancingCases } from './src/device_financing/cases';

// Get cases and split
const allCases = getDeviceFinancingCases();
const trainCases = allCases.slice(0, 6);
const testCases = allCases.slice(6);

// Train
agent.train(trainCases);

// Evaluate
const metrics = agent.evaluate(testCases);
console.log('Accuracy:', metrics.accuracy + '%');
```

## 📚 Next Steps

1. **Read the Full README**: [README.md](README.md) for detailed documentation
2. **Follow Learning Guide**: [LEARNING_GUIDE.md](LEARNING_GUIDE.md) for step-by-step tutorials
3. **Review Cases**: Check [src/device_financing/cases.ts](src/device_financing/cases.ts) for all 8 scenarios
4. **Explore Agent Code**: Study [src/agents/index.ts](src/agents/index.ts) to understand decision logic
5. **Run Tests**: `npm test` to see comprehensive test coverage

## 🎓 Learning Path

### Beginner (30 minutes)
- ✅ Run demos (`npm run demo`)
- ✅ Try API endpoints
- ✅ Read case scenarios in `cases.ts`

### Intermediate (2 hours)
- ✅ Create custom agent configurations
- ✅ Train agents on different case splits
- ✅ Compare agent strategies
- ✅ Follow Learning Guide exercises

### Advanced (4+ hours)
- ✅ Implement custom scoring logic
- ✅ Add new device categories
- ✅ Integrate ML models
- ✅ Build multi-agent systems

## 🔧 Troubleshooting

**Issue**: TypeScript compilation errors
```bash
npm install
npm run build
```

**Issue**: Port 3000 already in use
```bash
# Set custom port
PORT=3001 npm start
```

**Issue**: Missing dependencies
```bash
npm install express body-parser typescript ts-node
npm install --save-dev @types/express @types/node jest ts-jest
```

## 📖 Key Files

| File | Purpose |
|------|---------|
| `src/agents/index.ts` | Core agent implementation |
| `src/device_financing/cases.ts` | 8 financing scenarios |
| `src/examples/agent_demo.ts` | 6 interactive demos |
| `src/tests/agent.test.ts` | Comprehensive tests |
| `src/app.ts` | REST API server |
| `LEARNING_GUIDE.md` | Complete tutorial |

## 🎯 Common Use Cases

**Use Case 1: Find best option for high credit customer**
```typescript
const highCreditCase = getFinancingCaseById(1);
const decision = agent.analyzeFinancingCase(highCreditCase);
```

**Use Case 2: Handle low credit scenario**
```typescript
const lowCreditCase = getFinancingCaseById(4);
const decision = agent.analyzeFinancingCase(lowCreditCase);
```

**Use Case 3: Business/corporate purchase**
```typescript
const corporateCase = getFinancingCaseById(3);
const decision = agent.analyzeFinancingCase(corporateCase);
```

## 💡 Tips

1. **Start with demos**: Run `npm run demo` to see everything in action
2. **Experiment with weights**: Try different agent configurations
3. **Review test cases**: Check `agent.test.ts` for usage examples
4. **Use API docs**: Visit `/api/docs` for complete endpoint reference
5. **Read case details**: Each case has rich context for learning

## 🚀 You're Ready!

You now have everything you need to:
- ✅ Create intelligent financing agents
- ✅ Analyze device financing scenarios
- ✅ Train and evaluate agent performance
- ✅ Build production-ready AI systems

**Happy Learning! 🤖**

Need help? Check:
- 📖 [Full README](README.md)
- 📚 [Learning Guide](LEARNING_GUIDE.md)
- 🧪 [Tests](src/tests/agent.test.ts)
- 🎯 [Demos](src/examples/agent_demo.ts)
