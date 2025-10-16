from flask import Flask, render_template

# Flask एप्लिकेशन को इनिशियलाइज़ करना
app = Flask(__name__)

# --- Home Page Route ---
@app.route('/')
def home():
    """
    मुख्य पृष्ठ (Home Page) को रेंडर करता है।
    यह 'index.html' टेम्पलेट को ढूंढेगा और प्रदर्शित करेगा।
    """
    # आप यहां होम पेज के लिए डायनामिक डेटा (जैसे नाम, टाइटल, आदि) पास कर सकते हैं।
    return render_template('home.html', title='Home')

# --- About Page Route ---
@app.route('/about')
def about():
    """
    'मेरे बारे में' पृष्ठ (About Page) को रेंडर करता है।
    यह 'about.html' टेम्पलेट को ढूंढेगा और प्रदर्शित करेगा।
    """
    # आप यहां 'About' सेक्शन का डेटा पास कर सकते हैं।
    return render_template('about.html', title='About')

@app.route('/projects')
def projects():
    """
    'प्रोजेक्ट्स' पृष्ठ (Projects Page) को रेंडर करता है।
    यह 'projects.html' टेम्पलेट को ढूंढेगा और प्रदर्शित करेगा।
    """
    # आप यहां प्रोजेक्ट्स की एक सूची (list of projects) पास कर सकते हैं।
    return render_template('projects.html', title='Projects')

# --- Skills Page Route ---
@app.route('/skills')
def skills():
    """
    'कौशल' पृष्ठ (Skills Page) को रेंडर करता है।
    यह 'skills.html' टेम्पलेट को ढूंढेगा और प्रदर्शित करेगा।
    """
    # आप यहां स्किल्स की एक सूची (list of skills) पास कर सकते हैं।
    return render_template('skills.html', title='Skills')

# --- Contact Page Route ---
@app.route('/contact')
def contact():
    """
    'संपर्क' पृष्ठ (Contact Page) को रेंडर करता है।
    यह 'contact.html' टेम्पलेट को ढूंढेगा और प्रदर्शित करेगा।
    """
    # आप यहां संपर्क फॉर्म हैंडलिंग लॉजिक जोड़ सकते हैं।
    return render_template('contact.html', title='Contact')


# एप्लिकेशन को रन करना
if __name__ == '__main__':
    # 'debug=True' से डेवलपमेंट के दौरान कोड में बदलाव करने पर सर्वर अपने आप रीलोड हो जाता है।
    # जब आप इसे डिप्लॉय करें, तो 'debug=False' करना न भूलें।
    print("Flask App चल रहा है। ब्राउज़र में http://127.0.0.1:5000/ पर जाएँ।")
    app.run(debug=True)
