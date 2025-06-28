
# Pilikula

**Pilikula Project** is a beginner-friendly Flask web application that highlights the top 5 attractions in Pilikula, a cultural and ecological hub. It offers a clean, interactive, and user-friendly interface to provide detailed insights into these attractions. Perfect for learners and hobbyists, this project demonstrates essential Flask functionalities like dynamic routing and responsive design.

---

## 🌟 Features

- **Dynamic Pages**: Each attraction has its own beautifully designed and dynamically rendered page.
- **Responsive Design**: Styled with CSS to ensure a seamless and engaging user experience.
- **Custom Error Handling**: Displays a friendly and informative 404 error page.
- **Static Assets**: Includes images, styles, and scripts for a polished application experience.
- **Beginner-Friendly**: Perfect for anyone starting their journey with Flask and Python.

---

## 🗂️ Project Structure

```
pilikula/
├── app.py             # Main application file (Flask backend)
├── data.py            # Data for rendering attractions
├── static/
│   ├── park.jpg       # Images for attractions
│   ├── script.js      # JavaScript for interactivity
│   ├── styles.css     # CSS for styling
│   ├── images/        # Additional attraction images
├── templates/
│   ├── 404.html       # Custom error page
│   ├── base.html      # Base template layout
│   ├── index.html     # Homepage template
│   ├── place.html     # Individual attraction pages
└── __pycache__/       # Python cache files
```

---

## 🚀 How to Run

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/codemy3/pilikula.git
   cd pilikula
   ```

2. **Install Dependencies**:  
   ```bash
   pip install flask
   ```

3. **Run the Application**:  
   ```bash
   python app.py
   ```

4. **Open in Browser**:  
   Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) to explore the application.

---

## 📸 Screenshots

Add some visuals to bring your project to life:  
- **Homepage**: Showcase the main attractions.  
- **Attraction Page**: Highlight detailed information about a place.  
- **404 Page**: Friendly error page.

---

## 🌱 Future Enhancements

- **Search Functionality**: Quickly locate attractions using a search bar.
- **User Reviews**: Allow users to rate and review attractions.
- **Interactive Maps**: Integrate Google Maps for location display.
- **Admin Dashboard**: Enable admins to add, update, or delete attractions.

---

## 🤝 Contributing

Contributions are welcome! Here’s how you can help:  
1. Fork this repository.  
2. Create a new branch: `git checkout -b feature-name`.  
3. Make your changes and commit: `git commit -m 'Added feature'`.  
4. Push to the branch: `git push origin feature-name`.  
5. Submit a pull request for review.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgments

- **Flask**: For providing an easy and robust web framework.
- **Bootstrap**: For modern and responsive web design elements.
- **Contributors**: Thank you to everyone who helped enhance this project.
