# VSGEO

![icon](https://user-images.githubusercontent.com/100694366/213791818-115e2bc7-9561-4503-b204-404628a19914.png)

Open Source Intellegent Tool for VSCO

## Getting Started

### Installing
To install:
```
 $ git clone https://github.com/CanavarB/VSGEO.git # Clone the repo
 $ cd VSGEO                                        # Change the directory
 $ pip install .                                   # Install with pip
```
## Usage

To scrape location info from a VSCO user:
```
 $ vsgeo <username> --location
```
or:
```
 $ vsgeo <username> -l
```
_If user's images have location info it will print_

Example:

https://user-images.githubusercontent.com/100694366/213791959-efa2302e-10e4-433a-a925-11ab8fae2919.mp4


## Options

| Option               | Secondary Options | Description                                                                                                                               |
| -------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| --location           | -l                | Scrapes all location information of users in a human-readable way.                                                                                                        |
| --coords             | -c                | Scrapes users all location information with coordinates.
| --device             | -d                | Scrapes all device information, make and model information from user.
| --raw                | -r                | Scrapes all data from user media and displays it in JSON format.
| --border             | -b                | It does all the features mentioned above in the same way, but with the given media number or the given range.                                                                                                              |

## Author

- **Canavar B.** - _Initial work_ - [CanavarB](https://github.com/CanavarB)

### Inspired By

- **Mustafa Abdi**  - [_vsco-scraper_](https://github.com/mvabdi/vsco-scraper)

## License

This project is licensed under the MIT License.
