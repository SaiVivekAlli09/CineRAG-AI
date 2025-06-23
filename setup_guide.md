📄 setup_guide.md

# 🛠️ CineRAG-AI Setup Guide

Complete installation guide for CineRAG-AI - explained in simple terms!

## 📋 What You Need First

### **Your Computer Needs:**
- **Python 3.8 or newer** (like having the right version of an app)
- **4GB RAM minimum** (8GB is better for smooth running)
- **2GB free space** (for downloading AI tools)
- **Internet connection** (to download the smart AI brain)

### **Accounts You Need:**
- **GitHub account** (free at github.com)
- **That's it!** No other accounts required

---

## 🪟 Windows Setup (Step-by-Step)

### **Step 1: Install Python**
1. Go to **python.org** in your web browser
2. Click the big yellow "Download Python" button
3. **SUPER IMPORTANT**: When installing, check the box that says "Add Python to PATH"
4. Click "Install Now"
5. **Test it worked**: Open Command Prompt (type "cmd" in start menu) and type:
   ```cmd
   python --version


Step 2: Get Your Project

   # Open Command Prompt and type these one by one:

# Go to your Downloads folder (or wherever you want the project)
cd Downloads

# Download CineRAG-AI from GitHub
git clone https://github.com/yourusername/CineRAG-AI.git

# Go into the project folder
cd CineRAG-AI

Step 3: Install the AI Tools

# This downloads all the smart tools your project needs
pip install -r requirements.txt

# If you get an error, try this instead:
pip install --user -r requirements.txt

Step 4: Run CineRAG-AI!
cmdpython main.py
What should happen: You see the CineRAG-AI menu! 🎉


✅ Test Everything Works
Quick Test Script
Create a file called test.py and put this in it:
python# test.py - Check if everything works
try:
    import numpy as np
    import sentence_transformers
    print("✅ All tools installed successfully!")
    
    # Test the AI brain
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("✅ AI brain loaded successfully!")
    print("🎬 CineRAG-AI is ready!")
    
except ImportError as e:
    print(f"❌ Missing tool: {e}")
    print("💡 Run: pip install -r requirements.txt")
except Exception as e:
    print(f"❌ Problem: {e}")
Run it:
bashpython test.py
What Success Looks Like
When everything works, you should see:
✅ All tools installed successfully!
✅ AI brain loaded successfully!
🎬 CineRAG-AI is ready!

🎬 Your First CineRAG-AI Experience
What Happens When You First Run It:

Loading (30 seconds): The AI brain downloads and loads
Welcome Screen: You see the CineRAG-AI menu
Sample Movies Added: 15 popular movies are added automatically
Ready to Go: You can start searching immediately!

Try These First Searches:

"action movies"
"funny films for kids"
"sci-fi with good ratings"
"movies like Marvel"

Train the AI:

Like movies you recognize
Dislike movies you don't like
Watch how recommendations get better!


🆘 Getting More Help
If You're Still Stuck:

Read the error message carefully - it usually tells you what's wrong
Google the exact error - someone else probably had the same problem
Ask on GitHub: Go to the Issues section of the CineRAG-AI repository
Check if your Python version is 3.8+: Some tools need newer Python

Common Beginner Mistakes:

❌ Forgetting to check "Add Python to PATH"
❌ Using python instead of python3 on Mac/Linux
❌ Not being in the right folder when running commands
❌ Having spaces in folder names (use CineRAG-AI, not "Cine RAG AI")

Pro Tips:

✅ Always read error messages - they're trying to help!
✅ Copy-paste commands exactly as written
✅ One command at a time - don't rush
✅ Ask for help if stuck - the programming community is friendly!


🎯 You Did It!
Once CineRAG-AI is running, you've successfully:

✅ Installed Python and tools like a developer
✅ Downloaded and ran an AI project
✅ Set up a machine learning system
✅ Joined the AI developer community

That's genuinely impressive! You're now running the same type of AI technology used by Netflix, Spotify, and ChatGPT. 🚀
Welcome to the world of AI development! 🤖✨
