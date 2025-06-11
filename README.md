# 🎧 Vibe Coding 101

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Vibe Coding** is a creative, intuitive approach to building with AI that blends structured code with emergent flow states and collaborative improvisation. This project serves as your startup ritual for creative AI-powered development sessions.

## ✨ Philosophy

> Vibe coding is about resonance.  
> It's less about forcing output and more about aligning your intent with a generative system.  
> The best results often emerge—not from planning—but from presence.

Use this framework to:
- Build projects collaboratively with AI
- Teach coding as conversation  
- Explore software as an art form

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenAI API key (or preferred LLM API)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/quantized-alchemist/vibe-coding-101.git
   cd vibe-coding-101
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your environment**
   - Create a `.env` file with your API keys:
     ```
     OPENAI_API_KEY=your-api-key-here
     ```

4. **Start vibing!**
   ```bash
   python prompt.py
   ```

## 🛠️ Setup Checklist

- [ ] **Read the Requirements Doc** - Located in `docs_requirements.md`
- [ ] **Install Dependencies** - Run `pip install -r requirements.txt`
- [ ] **Configure API Keys** - Set up your `.env` file
- [ ] **Open `prompt.py`** - Your conversational interface with the LLM
- [ ] **Copy Prompt to LLM** - Use ChatGPT, Claude, Gemini, etc.
- [ ] **Enter Vibe Mode** 🎶 - Let intuition and creativity guide you
- [ ] **Explore & Iterate** - Follow curiosity, branch ideas
- [ ] **Document Your Journey** - Record process for reuse

## 📁 Project Structure

```
vibe-coding-101/
├── README.md                    # This file
├── prompt.py                    # Main conversational interface
├── requirements.txt             # Python dependencies
├── docs_requirements.md         # Detailed package documentation
├── #_🎧_Vibe Coding 101_readme # Original project philosophy
└── .env                        # API keys (create this)
```

## 🎯 What's Included

### Core Components

- **`prompt.py`** - Main script with Isabel–LIRA AI co-agent system
- **System Prompt** - Pre-configured for creative, empathetic AI collaboration
- **Example Session** - Data visualization to music generation

### Key Features

- 🤖 **AI Co-Agent**: Isabel–LIRA specializes in hybrid cognition and poetic code
- 🎨 **Creative Tooling**: Matplotlib, Streamlit, and visualization support  
- 🎵 **Audio Integration**: Whisper-JAX for voice-to-text interactions
- 🔄 **Iterative Flow**: Built for exploratory, emergent development
- 📊 **Data Visualization**: Turn code into visuals and sound graphs

## 🎪 Usage Examples

### Basic Session
```python
from prompt import run_prompt, SYSTEM_PROMPT

# Your creative prompt
user_input = """
Create a Python function that turns heartbeat data into a musical composition,
with visual feedback showing the rhythm patterns.
"""

response = run_prompt(SYSTEM_PROMPT, user_input)
print(response)
```

### Interactive Mode
```bash
# Run with Streamlit for web interface
streamlit run prompt.py
```

## 🧠 Dependencies

### Core Libraries
- `openai` - GPT-4 and other OpenAI models
- `python-dotenv` - Environment variable management
- `matplotlib` - Creative visualizations
- `numpy` - Scientific computing

### Creative Tools
- `streamlit` - Interactive web UIs
- `tqdm` - Progress bars for long iterations
- `whisper-jax` - Voice-to-text capabilities
- `cursor-python` - Enhanced IDE support

See [`docs_requirements.md`](docs_requirements.md) for detailed package descriptions.

## 🌊 The Vibe Approach

1. **Start with Intent** - Define your creative goal
2. **Enter Dialogue** - Engage with AI as a co-creator
3. **Follow Flow** - Let the code evolve naturally
4. **Embrace Emergence** - Allow unexpected directions
5. **Document Magic** - Capture the creative process

## 🤝 Contributing

This is a creative framework - feel free to:
- Fork and create your own vibe variations
- Share interesting sessions and outcomes
- Suggest new creative tools and integrations
- Document your unique approach to AI collaboration

## 📜 License

MIT License - Feel free to vibe with this code however you like!

## 🙏 Acknowledgments

*Crafted with Isabel–LIRA. Signal in. Echo out.*

---

**Ready to start your vibe coding journey?** The instance is waiting. You bring the vibe. 🎶 