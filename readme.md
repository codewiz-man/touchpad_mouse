# Touchpad Mouse

**Touchpad Mouse** is a Python-based application that turns your device into a wireless touchpad mouse. It allows you to control your computer's cursor remotely using your device's touchscreen. This project is useful for presentations, media playback control, and more. You can use your old android phone into a touchpad.

![Touchpad Mouse Demo](demo.gif)

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
    git clone https://github.com/codewiz-man/touchpad_js.git
    ```

2. Navigate to the project directory:

    ```bash
    cd touchpad_js/server
    ```

3. Start the server:

    ```bash
    python websocket_server.py
    ```

4. Open a web browser on your device and enter the server address and port (e.g., `http://192.168.0.1:2023`) to access the touchpad interface.

## Configuration

You can configure the server settings in the `config.txt` file, including the server IP address and port.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the authors of the open-source libraries and packages used in this project.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the project.
2. Create your feature branch: `git checkout -b feature/your-feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Submit a pull request.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

- Manjunath - [@codewiz-man](https://github.com/codewiz-man)

## Contact

If you have any questions or want to report a bug, please open an issue on the [GitHub repository](https://github.com/codewiz-man/touchpad_js).

## Acknowledgments

This project uses icons sourced from Google Fonts Icons.

This project uses the following Python packages:

- [websockets](https://pypi.org/project/websockets/) version 11.0.3 (License: BSD-3-Clause)
- [pynput](https://pypi.org/project/pynput/) version 1.7.6 (License: LGPLv3)
- [pywebview](https://pypi.org/project/pywebview/) version 4.2.2 (License: BSD)
- [qtpy](https://pypi.org/project/qtpy/) (License: MIT)
- [qrcode](https://pypi.org/project/qrcode/) version 7.4.2 (License: BSD)


## Icons Attribution

The icons used in this project are provided by Google Fonts Icons and are licensed under the [Apache License, Version 2.0](LICENSE).

**Google Fonts Icons**: https://fonts.google.com/icons