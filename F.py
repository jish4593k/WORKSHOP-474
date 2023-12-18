from server.app import app
from server.website import Website
from server.backend import BackendApi
from json import load
import torch
import scipy
import tkinter as tk
from tkinter import filedialog

class AdvancedAppRunner:
    def __init__(self, config_path='config.json'):
        self.config = load(open(config_path, 'r'))
        self.site_config = self.config.get('site_config', {})
        self.site = Website(app)
        self.backend_api = BackendApi(app, self.config)

    def register_routes(self, routes, entity):
        for route in routes:
            app.add_url_rule(
                route,
                view_func=entity.routes[route]['function'],
                methods=entity.routes[route]['methods'],
            )

    def _perform_advanced_operations(self):
        
        tensor_data = torch.randn(3, 3)
        eigenvalues, _ = torch.symeig(tensor_data)
        scipy_result = scipy.special.exp10(eigenvalues.numpy())
        return f"PyTorch Tensor: {tensor_data}\nEigenvalues: {eigenvalues}\nSciPy Result: {scipy_result}"

    def _show_gui(self, result):
        root = tk.Tk()
        root.title("Advanced App GUI")
        root.geometry("400x200")

        result_label = tk.Label(root, text=result, wraplength=380, justify='left')
        result_label.pack(pady=20)

        root.mainloop()

    def run_app(self):
        self.register_routes(self.site.routes, self.site)
        self.register_routes(self.backend_api.routes, self.backend_api)

        print(f"Running on port {self.site_config.get('port', 5000)}")

        
        advanced_result = self._perform_advanced_operations()

        
        self._show_gui(advanced_result)

        print(f"Closing the application")

if __name__ == '__main__':
    advanced_app_runner = AdvancedAppRunner()
    advanced_app_runner.run_app()
