import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt
import requests

class WeatherApp(QWidget):
    def _init_(self):
        super()._init_()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Weather App')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.weather_label = QLabel('')
        self.layout.addWidget(self.weather_label)

        self.location_input = QLineEdit()
        self.location_input.setPlaceholderText("Enter your city name here")
        self.location_input.setText("Bengaluru")  # Set default city name
        self.layout.addWidget(self.location_input)

        self.button = QPushButton('Get Weather')
        self.button.clicked.connect(self.get_weather)
        self.layout.addWidget(self.button)

    def get_weather(self):
        location = self.location_input.text()
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid=5d16c616e5035fce8016b4d43a57b384')
        data = response.json()

        if data['cod'] == 200:
            temp_k = data['main']['temp']
            temp_c = temp_k - 273.15  # Convert temperature from Kelvin to Celsius
            description = data['weather'][0]['description']
            self.weather_label.setText(f'Temperature: {temp_c:.2f}°C\nDescription: {description}')
        else:
            self.weather_label.setText('Error fetching weather data.')

if _name_ == '_main_':
    app = QApplication(sys.argv)
    ex = WeatherApp()
    ex.show()
    sys.exit(app.exec_())
