# ChatGPT plugins quickstart

Get a todo list ChatGPT plugin up and running in under 5 minutes using Python. If you do not already have plugin developer access, please [join the waitlist](https://openai.com/waitlist/plugins).

## Setup

To install the required packages for this plugin, run the following command:

```bash
pip install -r requirements.txt
```

To run the plugin, enter the following command:

```bash
python main.py
```

Once the local server is running:

1. Navigate to https://chat.openai.com. 
2. In the Model drop down, select "Plugins" (note, if you don't see it there, you don't have access yet).
3. Select "Plugin store"
4. Select "Develop your own plugin"
5. Enter in `localhost:5001` since this is the URL the server is running on locally, then select "Find manifest file".

The plugin should now be installed and enabled! You can start with a question like 
- "Which Bundestag protocols existed between May 2023 and today?" 
- "What activities have taken place between May 2023 and today?"

## Getting help

If you run into issues or have questions building a plugin, please join our [Developer community forum](https://community.openai.com/c/chat-plugins/20).


## Notes
The logo ["Eagle Icon"](https://www.iconarchive.com/show/animal-icons-by-martin-berube/eagle-icon.html) used for this demo plugin is from Martin Berube, please check the [license](https://www.iconarchive.com/icons/martin-berube/animal/terms-of-use.txt) for it.


# Disclaimer

This software plugin ("Bundestags Protokolle") is provided by the author Armin Hadzalic on an "as is" and "as available" basis for the sole purpose of demonstrating the functionality of ChatGPT plugins. It was created based on the ToDo Plugin from OpenAI. The Author makes no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability, or availability of the Plugin or the information, products, services, or related graphics contained within the Plugin for any purpose.

The Author hereby disclaims all warranties and conditions with regard to this Plugin, including all implied warranties and conditions of merchantability, fitness for a particular purpose, title, and non-infringement. In no event shall the Author be liable for any special, direct, indirect, consequential, or incidental damages or any damages whatsoever, whether in an action of contract, negligence or other tort, arising out of or in connection with the use of the Plugin or the contents of the Plugin.

The Plugin is intended for demonstration purposes only and is not intended for productive usage. Any reliance you place on such information is therefore strictly at your own risk. The Author does not warrant that the Plugin will be uninterrupted, timely, secure, or error-free, that the results that may be obtained from the use of the Plugin will be accurate or reliable, or that the quality of any products, services, information, or other material obtained by you through the Plugin will meet your expectations.

By using this Plugin, you expressly agree to these terms and conditions. If you do not agree with these terms, please do not download, install, or use the Plugin. The Author reserves the right to make changes or updates to the Plugin at any time without notice.
