import numpy as np
import matplotlib.pyplot as plt


class Signal:
    def __init__(self, name, values):
        self.name = name
        self.values = np.array(values, dtype=float)

    def mean_value(self):
        return np.mean(self.values)

    def min_value(self):
        return np.min(self.values)

    def max_value(self):
        return np.max(self.values)

    def plot(self):
        plt.figure(figsize=(10, 3))
        plt.plot(self.values, color="steelblue")
        plt.title(self.name)
        plt.xlabel("Vzorky")
        plt.ylabel("Amplituda")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def count_above(self, threshold):
        value_list = np.sum(self.values > threshold)
        return value_list


class ECGSignal(Signal):                              # ← závorka = dědíme od Signal
    def __init__(self, name, values, sampling_rate, lead="II"):
        super().__init__(name, values)                # ← zavolá __init__ rodiče
        self.sampling_rate = sampling_rate
        self.lead = lead

    def duration_seconds(self):
        return len(self.values) / self.sampling_rate

    def __str__(self):
        return (
            f"[{self.name}] svod={self.lead}, "
            f"vzorkování={self.sampling_rate} Hz, "
            f"délka={self.duration_seconds():.2f} s, "
            f"průměr={self.mean_value():.2f}"
        )


class RespirationSignal(Signal):
    def __init__(self, name, values, breathing_rate):
        super().__init__(name, values)
        self.breathing_rate = breathing_rate


ekg = ECGSignal(
    "EKG pacienta 42",
    [0.5, 1.2, 1.8, 0.9, 2.1, 1.5, 0.7, 1.1, 1.3, 0.8],
    sampling_rate=500,
    lead="I",
)

signal = RespirationSignal(
    "EKG pacienta 42",
    [0.5, 1.2, 1.8, 0.9, 2.1, 1.5, 0.7, 1.1, 1.3, 0.8],
    60
)

# Metody zděděné ze Signal – ECGSignal je nikde nedefinuje, přesto fungují:
print(ekg.mean_value())    # 1.19
print(ekg.max_value())     # 2.1
ekg.plot()                 # vykreslí graf

# Vlastní metody ECGSignal:
print(f"Délka záznamu: {ekg.duration_seconds():.3f} s")
print(f"Svod: {ekg.lead}")

# __str__ je definovaná v ECGSignal, takže print používá tuhle verzi:
print(ekg)
# [EKG pacienta 42] svod=I, vzorkování=500 Hz, délka=0.02 s, průměr=1.19

# skuska metody count_above
print(f"Pocet vzorkov presahujicich zadanu hranicu: {ekg.count_above(threshold=1)}")

# metody pre RespirationSignal
signal.plot()
print(f"Dychova frekvencia : {signal.breathing_rate} dychov/min")