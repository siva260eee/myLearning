# AI & ML Learning Journey 🚀

Welcome to your comprehensive AI and Machine Learning learning path! This structured curriculum will take you from ML fundamentals through to building AI agents and working with the Model Context Protocol.

## 🗺️ Learning Path Overview

```
01_ML_Fundamentals → 02_Deep_Learning → 03_NLP_LLMs → 04_AI_Agents → 05_MCP → 06_Projects
```

## 📚 Modules

### [01_ML_Fundamentals](./01_ML_Fundamentals/)
**Duration**: 2-3 weeks  
**Prerequisites**: Python basics (completed!)

**What You'll Learn**:
- Supervised, Unsupervised, Reinforcement Learning
- Key algorithms: Linear/Logistic Regression, Decision Trees, Random Forests, SVM, KNN
- Data preprocessing and feature engineering
- Model evaluation and cross-validation
- Scikit-learn library

**Key Projects**:
- House price prediction
- Customer churn classifier
- Complete ML pipeline

---

### [02_Deep_Learning](./02_Deep_Learning/)
**Duration**: 3-4 weeks  
**Prerequisites**: ML Fundamentals

**What You'll Learn**:
- Neural networks and backpropagation
- CNNs for computer vision
- RNNs and LSTMs for sequences
- Transfer learning
- TensorFlow/Keras or PyTorch
- Regularization techniques

**Key Projects**:
- Image classifier (MNIST, CIFAR-10)
- Sentiment analysis
- Transfer learning application
- GAN for image generation

---

### [03_NLP_LLMs](./03_NLP_LLMs/)
**Duration**: 3-4 weeks  
**Prerequisites**: Deep Learning

**What You'll Learn**:
- Text preprocessing and embeddings
- Transformers and attention mechanism
- BERT, GPT, T5 architectures
- Large Language Models (GPT-4, Claude, Gemini)
- Prompt engineering
- Retrieval Augmented Generation (RAG)
- Fine-tuning techniques (LoRA, QLoRA)

**Key Projects**:
- Text classification with BERT
- Build a RAG system
- Prompt engineering experiments
- Fine-tune a small LLM

---

### [04_AI_Agents](./04_AI_Agents/)
**Duration**: 2-3 weeks  
**Prerequisites**: NLP & LLMs

**What You'll Learn**:
- Agent architectures (ReAct, etc.)
- Tool usage and function calling
- Memory systems
- Planning and reasoning
- Multi-agent systems
- LangChain and LlamaIndex
- Agent evaluation and safety

**Key Projects**:
- Research assistant agent
- Code analysis agent
- Multi-tool agent
- Multi-agent collaboration

---

### [05_MCP](./05_MCP/)
**Duration**: 2-3 weeks  
**Prerequisites**: AI Agents

**What You'll Learn**:
- Model Context Protocol fundamentals
- Building MCP servers (TypeScript/Python)
- MCP primitives: Tools, Resources, Prompts
- Security model
- Integration with Claude Desktop
- Deploying MCP servers

**Key Projects**:
- File system MCP server
- Database integration server
- Custom tool server
- Full application with MCP

---

### [06_Projects](./06_Projects/)
**Duration**: Ongoing

**Capstone Projects**:
1. Complete AI application
2. Custom AI agent with MCP
3. Domain-specific LLM application
4. Contribution to open source

---

## 🚀 Getting Started

### 1. Prerequisites Check
Make sure you've completed:
- [ ] Python Basics (01_Basics)
- [ ] Control Flow (02_Control_Flow)
- [ ] Functions (03_Functions)
- [ ] OOP (04_OOP)
- [ ] Data Structures (05_DataStructures)

### 2. Environment Setup

#### Install Core Libraries
```bash
# ML Fundamentals
pip install numpy pandas scikit-learn matplotlib seaborn

# Deep Learning
pip install tensorflow  # or pytorch
pip install keras

# NLP & LLMs
pip install transformers datasets
pip install openai anthropic  # For API access
pip install langchain langchain-community
pip install chromadb  # Vector database

# AI Agents
pip install langchain-openai
pip install langgraph

# MCP
npm install -g @modelcontextprotocol/create-server
```

#### Optional but Recommended
```bash
# Jupyter for experiments
pip install jupyter ipykernel

# Additional tools
pip install plotly  # Interactive plots
pip install huggingface-hub  # Model hub
pip install sentence-transformers  # Embeddings
```

### 3. Get API Keys (When Needed)

For LLM modules, you'll eventually need:
- **OpenAI API** (GPT models): https://platform.openai.com/
- **Anthropic API** (Claude): https://console.anthropic.com/
- **Hugging Face**: https://huggingface.co/ (free, for open models)

**💡 Tip**: Start with free/open-source models, get paid APIs later!

### 4. Hardware Considerations

**For Most Exercises**:
- CPU is fine for learning
- 8GB RAM minimum
- 16GB RAM recommended

**For Deep Learning Training**:
- GPU highly recommended
- **Free Options**:
  - Google Colab (free GPU)
  - Kaggle Kernels (free GPU)
  - Paperspace free tier

---

## 📖 How to Use This Curriculum

### Each Module Contains

```
Module/
  ├── CONCEPTS.md       # Theory and explanations
  ├── examples.py       # Working code examples
  ├── EXERCISES.md      # Practice problems
  └── my_solutions.py   # Your solutions go here
```

### Study Approach

1. **Read CONCEPTS.md**: Understand theory
2. **Run examples.py**: See concepts in action
3. **Try EXERCISES.md**: Practice yourself
4. **Code in my_solutions.py**: Write your solutions
5. **Build projects**: Apply knowledge
6. **Review and iterate**: Reinforce learning

### Time Commitment

**Intensive**: 15-20 hours/week → 3-4 months total  
**Regular**: 8-10 hours/week → 6-8 months total  
**Casual**: 4-5 hours/week → 12+ months total

**Remember**: Quality > Speed. Make sure you understand before moving on!

---

## 🎯 Learning Goals

By the end of this journey, you will be able to:

- [ ] Build and deploy machine learning models
- [ ] Create deep learning applications for vision and text
- [ ] Work with Large Language Models and APIs
- [ ] Design and implement AI agents
- [ ] Build MCP servers for modular AI capabilities
- [ ] Develop complete AI-powered applications
- [ ] Understand current AI research and trends
- [ ] Contribute to AI projects

---

## 🛠️ Tools & Technologies

### Languages
- **Python**: Primary language (you know this!)
- **TypeScript**: For MCP servers (you'll learn)

### Libraries & Frameworks
- **scikit-learn**: Traditional ML
- **TensorFlow/Keras** or **PyTorch**: Deep Learning
- **Transformers**: Pre-trained models
- **LangChain**: Agent orchestration
- **LlamaIndex**: Data indexing
- **MCP SDK**: Protocol implementation

### Platforms
- **Jupyter**: Interactive development
- **Google Colab**: Free GPU computing
- **Hugging Face**: Model hub
- **GitHub**: Version control
- **Claude Desktop**: MCP integration

---

## 📊 Progress Tracking

Create a `PROGRESS.md` file to track your journey:

```markdown
# My AI/ML Progress

## Week 1
- [x] Started ML Fundamentals
- [x] Completed Linear Regression exercises
- [ ] Working on Classification

## Week 2
...
```

---

## 💡 Tips for Success

### 1. Practice Daily
Even 30 minutes per day > 4 hours once a week

### 2. Build Projects
Apply concepts immediately in small projects

### 3. Join Communities
- Hugging Face Forums
- r/MachineLearning
- LangChain Discord
- MCP Discord
- Local AI meetups

### 4. Read Papers
Start with blog posts, then papers:
- distill.pub
- Towards Data Science
- Papers with Code

### 5. Experiment
- Modify examples
- Break things
- Try different approaches
- Learn from failures

### 6. Document Learning
- Write blog posts
- Create tutorials
- Share on GitHub
- Teach others

### 7. Stay Updated
AI moves fast! Follow:
- Twitter/X: AI researchers
- Newsletters: The Batch, ImportAI
- Podcasts: Lex Fridman, TWIML
- YouTube: Two Minute Papers

---

## 🎓 Certificates & Validation

While this curriculum doesn't offer certificates, you can:

1. **Build Portfolio**: GitHub with projects
2. **Write Blog**: Share your learning
3. **Kaggle Competitions**: Validate skills
4. **Contribute to OSS**: Real-world experience
5. **Official Certifications** (optional):
   - TensorFlow Developer Certificate
   - AWS ML Specialty
   - Azure AI Engineer

---

## 📚 Additional Resources

### Books
- **Hands-On ML** (Aurélien Géron)
- **Deep Learning** (Goodfellow, Bengio, Courville)
- **Speech and Language Processing** (Jurafsky & Martin)

### Courses (Free)
- Fast.ai Practical Deep Learning
- Stanford CS229 (Machine Learning)
- Stanford CS224N (NLP)
- Stanford CS231N (CNNs)

### Websites
- Hugging Face Courses
- Google ML Crash Course
- OpenAI Cookbook
- LangChain Documentation

---

## 🤝 Getting Help

**Stuck? Here's what to do**:

1. **Re-read concepts**: Often clarity comes with re-reading
2. **Check examples**: See how it's done
3. **Google the error**: Someone had this problem before
4. **Ask AI assistants**: Claude, ChatGPT can help explain
5. **Community forums**: Post your question
6. **Take a break**: Sometimes you just need rest

**Remember**: Everyone struggles. Persistence matters more than perfection!

---

## 🎉 Let's Begin!

Ready to start your AI/ML journey? 

👉 **Go to [01_ML_Fundamentals](./01_ML_Fundamentals/) to begin!**

Or if you prefer a quick overview first, check out [START_HERE.md](./START_HERE.md)

---

## 📝 Notes

- This curriculum is self-paced
- Examples are beginner-friendly
- Gradually increases in complexity
- Focus on practical applications
- Based on industry best practices

**Your AI journey starts now! 🚀**

---

*Last updated: January 2026*  
*Based on current state-of-the-art in AI/ML*
