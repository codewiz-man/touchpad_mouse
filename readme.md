# Touchpad Mouse

**Touchpad Mouse** is a Python/Web based application that turns your device into a wireless touchpad mouse. It allows you to control your computer's cursor remotely using your device's touchscreen. This project is useful for presentations, media playback control, and more. You can use your old android phone as touchpad.

<p align="center">
  <img width="240" height="320" src="https://github.com/codewiz-man/touchpad_mouse/assets/39612669/e0679aea-3a0d-4898-b3bf-05797506fd71">
</p>


## Features

- Wireless touchpad mouse functionality.
- Left and right mouse button control.
- Scrolling support.
- Easy-to-use web interface for controlling your computer.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.5 or higher installed on your computer.
- Python packages listed in `requirements.txt` installed. You can install them using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Clone this repository to your computer:

    ```bash
    git clone https://github.com/codewiz-man/touchpad_mouse.git
    ```

2. Navigate to the project directory:

    ```bash
    cd touchpad_mouse/server
    ```

3. Start the server:

    ```bash
    python websocket_server.py
    ```

4. Open 'client/index.html' in web browser on your mobile phone or install the 'client/app-debug.apk'

## Configuration

You can configure the server settings in the `config.json` file, including the server port and sensitivity.

## Disclaimer

**Note:** This application is currently under development and has not undergone extensive testing. It may be unstable and should be used with caution. Please report any issues you encounter, and consider contributing to its development.

While we strive to maintain the quality and stability of this software, we cannot guarantee its performance in all environments or use cases. Use this application at your own risk.

Your feedback and contributions are highly appreciated as they can help improve the reliability and functionality of this project.

Thank you for your understanding.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the authors of the open-source libraries and packages used in this project.

## Authors

- manjunath - [@codewiz-man](https://github.com/codewiz-man)

## Contact

If you have any questions or want to report a bug, please open an issue on the [GitHub repository](https://github.com/codewiz-man/touchpad_js).

## Dependencies

This project uses icons sourced from Google Fonts Icons.

This project uses the following Python packages:

- [websockets](https://pypi.org/project/websockets/) version 11.0.3 (License: BSD-3-Clause)
- [pynput](https://pypi.org/project/pynput/) version 1.7.6 (License: LGPLv3)
- [pywebview](https://pypi.org/project/pywebview/) version 4.2.2 (License: BSD)
- [qrcode](https://pypi.org/project/qrcode/) version 7.4.2 (License: BSD)
- [pyinstaller](https://pypi.org/project/pyinstaller/) version 5.13.2 (License: GPL 2.0, Apache 2.0)


## Icons Attribution

The icons used in this project are provided by Google Fonts Icons and are licensed under the [Apache License, Version 2.0](LICENSE).

**Google Fonts Icons**: https://fonts.google.com/icons
