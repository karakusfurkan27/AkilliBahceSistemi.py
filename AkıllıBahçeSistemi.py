import tkinter as tk
from tkinter import ttk
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json
import time

# Varsayılan bitki profilleri
PLANT_PROFILES = {
    "Domates": {
        "temperature": (20, 30),
        "humidity": (50, 70),
        "soil_moisture": (40, 70),
        "light_level": (60, 80)
    },
    "Fesleğen": {
        "temperature": (18, 28),
        "humidity": (40, 60),
        "soil_moisture": (50, 80),
        "light_level": (50, 70)
    },
    "Biber": {
        "temperature": (18, 32),
        "humidity": (50, 70),
        "soil_moisture": (40, 60),
        "light_level": (70, 90)
    },
    "Marul": {
        "temperature": (15, 25),
        "humidity": (60, 80),
        "soil_moisture": (60, 90),
        "light_level": (40, 60)
    }
}

# Bitki profillerini kaydetmek için dosya yolu
PROFILE_FILE = "plant_profiles.json"

# Sensör verilerini simüle eden fonksiyon
def get_sensor_data():
    return {
        "temperature": random.uniform(15, 35),  # Sıcaklık (°C)
        "humidity": random.uniform(30, 80),     # Nem (%)
        "soil_moisture": random.uniform(0, 100),  # Toprak nemi (%)
        "light_level": random.uniform(0, 100)    # Işık seviyesi (%)
    }

def load_profiles():
    """Bitki profillerini kaydedilen dosyadan yükle"""
    try:
        with open(PROFILE_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return PLANT_PROFILES  # Eğer dosya yoksa varsayılan profilleri kullan

def save_profiles():
    """Bitki profillerini dosyaya kaydet"""
    with open(PROFILE_FILE, 'w') as f:
        json.dump(PLANT_PROFILES, f)

class GardenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Akıllı Bahçe Sistemi")
        self.root.geometry("900x700")
        self.root.configure(bg="#eef7e5")  # Arka plan: açık yeşil
        
        # Başlık
        title = tk.Label(self.root, text="Akıllı Bahçe Sistemi", font=("Helvetica", 16, "bold"), bg="#eef7e5", fg="#4caf50")
        title.pack(pady=10)
        
        # Bitki türü seçimi
        plant_label = tk.Label(self.root, text="Bitki Türü Seçin:", font=("Helvetica", 12), bg="#eef7e5")
        plant_label.pack()
        self.plant_type = ttk.Combobox(self.root, values=list(PLANT_PROFILES.keys()))
        self.plant_type.pack(pady=5)
        self.plant_type.set("Domates")  # Varsayılan
        
        # Yeni ürün ekleme alanı
        add_product_frame = tk.Frame(self.root, bg="#eef7e5")
        add_product_frame.pack(pady=10, padx=10, fill="x")
        
        tk.Label(add_product_frame, text="Yeni Ürün Adı:", bg="#eef7e5", font=("Helvetica", 12)).grid(row=0, column=0, padx=5, pady=5)
        self.new_product_name = tk.Entry(add_product_frame, font=("Helvetica", 12))
        self.new_product_name.grid(row=0, column=1, padx=5, pady=5)
        
        add_product_button = tk.Button(add_product_frame, text="Yeni Ürün Ekle", command=self.add_new_product, bg="#4caf50", fg="white", font=("Helvetica", 12))
        add_product_button.grid(row=0, column=2, padx=10)
        
        # Sistem durumu ve öneriler
        self.status_label = tk.Label(self.root, text="Sistem Durumu: Durdu", font=("Helvetica", 12, "bold"), bg="#eef7e5", fg="red")
        self.status_label.pack(pady=10)
        
        # Sensör verileri ve öneriler bölümü
        self.sensor_frame = tk.Frame(self.root, bg="#d6e9ce")
        self.sensor_frame.pack(pady=10, fill="x")
        
        self.sensor_labels = {}
        for sensor in ["temperature", "humidity", "soil_moisture", "light_level"]:
            label = tk.Label(self.sensor_frame, text=f"{sensor.capitalize()}: ---", font=("Helvetica", 12), bg="#d6e9ce", anchor="w")
            label.pack(fill="x", padx=10, pady=2)
            self.sensor_labels[sensor] = label
        
        self.recommendations_text = tk.Text(self.root, height=8, wrap="word", font=("Helvetica", 10), bg="#f8f8f8", fg="#333333")
        self.recommendations_text.pack(pady=10, padx=10, fill="both", expand=True)
        self.recommendations_text.insert("end", "Sistemi başlatın ve sensör verilerini güncelleyin...\n")
        
        # Sensör verilerini grafikle görselleştirme
        self.graph_frame = tk.Frame(self.root, bg="#eef7e5")
        self.graph_frame.pack(pady=10, fill="x")
        
        self.plot_button = tk.Button(self.graph_frame, text="Verileri Görselleştir", command=self.plot_data, bg="#4caf50", fg="white", font=("Helvetica", 12))
        self.plot_button.pack(pady=10)
        
        # Düğmeler (Yan Yana)
        button_frame = tk.Frame(self.root, bg="#eef7e5")
        button_frame.pack(pady=10)
        
        start_button = tk.Button(button_frame, text="Sistemi Başlat", command=self.start_system, bg="#4caf50", fg="white", font=("Helvetica", 12))
        start_button.grid(row=0, column=0, padx=5)
        
        stop_button = tk.Button(button_frame, text="Sistemi Durdur", command=self.stop_system, bg="#f44336", fg="white", font=("Helvetica", 12))
        stop_button.grid(row=0, column=1, padx=5)
        
        update_button = tk.Button(button_frame, text="Güncelle", command=self.update_data, bg="#388e3c", fg="white", font=("Helvetica", 12), state="disabled")
        update_button.grid(row=0, column=2, padx=5)
        self.update_button = update_button
        
        quit_button = tk.Button(button_frame, text="Çıkış", command=self.root.quit, bg="#9e9e9e", fg="white", font=("Helvetica", 12))
        quit_button.grid(row=0, column=3, padx=5)

        # Bitki profillerini yükle
        self.load_profiles()

    def start_system(self):
        self.status_label.config(text="Sistem Durumu: Çalışıyor", fg="green")
        self.update_button.config(state="normal")
        self.recommendations_text.insert("end", "\nSistem başlatıldı. Artık sensör verilerini güncelleyebilirsiniz.\n")
    
    def stop_system(self):
        self.status_label.config(text="Sistem Durumu: Durdu", fg="red")
        self.update_button.config(state="disabled")
        self.recommendations_text.insert("end", "\nSistem durduruldu. Güncellemeler devre dışı bırakıldı.\n")
    
    def update_data(self):
        plant_type = self.plant_type.get()
        sensor_data = get_sensor_data()
        
        for key, value in sensor_data.items():
            self.sensor_labels[key].config(text=f"{key.capitalize()}: {value:.2f}")
        
        self.recommendations_text.insert("end", f"\n'{plant_type}' için sensör verileri güncellendi.\n")
        
        # Bitki için öneri
        self.provide_recommendations(sensor_data)
    
    def add_new_product(self):
        name = self.new_product_name.get().strip()
        if name and name not in PLANT_PROFILES:
            temp = (20, 30)
            humidity = (50, 70)
            soil_moisture = (40, 70)
            light = (60, 80)
            
            PLANT_PROFILES[name] = {
                "temperature": temp,
                "humidity": humidity,
                "soil_moisture": soil_moisture,
                "light_level": light
            }
            
            self.plant_type["values"] = list(PLANT_PROFILES.keys())
            self.recommendations_text.insert("end", f"\nYeni ürün '{name}' başarıyla eklendi.\n")
            
            # Profil verilerini kaydet
            save_profiles()
        else:
            self.recommendations_text.insert("end", "\nGeçersiz veya mevcut bir bitki adı.\n")

    def provide_recommendations(self, sensor_data):
        recommendations = ""
        if sensor_data["temperature"] < 18:
            recommendations += "Sıcaklık çok düşük, bitkinin sıcaklık seviyesini arttırın.\n"
        elif sensor_data["temperature"] > 30:
            recommendations += "Sıcaklık çok yüksek, bitkilerinizi gölgeye alın.\n"
        
        if sensor_data["humidity"] < 40:
            recommendations += "Nem seviyesi düşük, bitkinizi sulayın.\n"
        elif sensor_data["humidity"] > 70:
            recommendations += "Nem seviyesi yüksek, havalandırmayı arttırın.\n"
        
        if sensor_data["soil_moisture"] < 30:
            recommendations += "Toprak nemi çok düşük, toprağı sulayın.\n"
        
        if sensor_data["light_level"] < 40:
            recommendations += "Işık seviyesi düşük, daha fazla ışık sağlamayı deneyin.\n"
        
        self.recommendations_text.insert("end", recommendations)

    def plot_data(self):
        sensor_data = get_sensor_data()
        fig, ax = plt.subplots(figsize=(6, 4))
        
        ax.bar(sensor_data.keys(), sensor_data.values(), color="green")
        ax.set_title("Sensör Verileri Görselleştirme")
        ax.set_xlabel("Sensörler")
        ax.set_ylabel("Değerler")
        
        # Etiketlerin daha görünür olması için eksenleri döndür
        plt.xticks(rotation=45, ha='right')
        
        # Tkinter içinde grafik gösterme
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.get_tk_widget().pack()
        canvas.draw()

    def load_profiles(self):
        """Bitki profillerini dosyadan yükle"""
        global PLANT_PROFILES
        PLANT_PROFILES = load_profiles()
        self.plant_type["values"] = list(PLANT_PROFILES.keys())

# Uygulamayı çalıştırma
if __name__ == "__main__":
    root = tk.Tk()
    app = GardenApp(root)
    root.mainloop()
