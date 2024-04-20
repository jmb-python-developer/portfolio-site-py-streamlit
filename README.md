# CV/Resume Site with Python and Streamlit

## Introduction
This portfolio site is built using Python and Streamlit, designed to showcase software development projects interactively. The site is structured to be easy to customize, making it perfect for developers looking to present their work in a professional and engaging manner.

## Getting Started
To get started with this portfolio site, you'll need to have Python installed on your machine, along with Streamlit. You can install Streamlit using pip:
```
pip install streamlit
```

## Project Structure
- `app.py`: The main Python script that runs the Streamlit application.
- `data/`: Directory where project data such as images, JSON files, or other project-related documents can be stored.
- `utils/`: Contains utility scripts or Python files that help in managing the application.

## How to Populate Your Information
### Adding Projects
To add your projects to the portfolio:
1. Navigate to the `data/` directory.
2. Add a new JSON file for each project with the following structure:
   ```json
   {
     "name": "Project Name",
     "description": "A brief description of the project.",
     "image_path": "path/to/image.jpg",
     "github_url": "https://github.com/yourusername/project-repo",
     "live_demo": "http://project-live-link.com",
     "technologies_used": ["Python", "Streamlit", "Other"]
   }
   ```
3. Make sure the `image_path` is relative to the `data/` directory.

### Customizing Appearance
- Modify the `app.py` to change the theme, layout, or add new sections to the website.
- Streamlit supports theming that can be configured in `app.py` or through `.streamlit/config.toml`.

## Running the Application
To run the application locally, navigate to the project directory in the terminal and run:
```
streamlit run app.py
```
This will start the server, and you can view your portfolio site by navigating to `http://localhost:8501` in your web browser.

## Deployment
For deploying your portfolio site, you can use Heroku, AWS, or any other cloud service provider that supports Python applications. Detailed steps for deployment can be found on the respective service provider's documentation.

## Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
This project is open source and available under the [MIT License](LICENSE).
