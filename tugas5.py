# FUNCTION
def greet(nama: str) -> str:
    return f"Halo, {nama}!"

def tambah(a: float, b: float = 0.0) -> float:
    return a + b

def rata_rata(angka: list[float]) -> float:
    if len(angka) == 0:
        return 0.0
    return round(sum(angka) / len(angka), 2)


# CLASS STUDENT
class Student:
    def __init__(self, nama: str, nim: str):
        self.nama: str = nama
        self.nim: str = nim
        self.nilai: list[float] = []

    def tambah_nilai(self, skor: float) -> None:
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        if self.rata_nilai() >= threshold:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    def __str__(self) -> str:
        return f"Student(nama='{self.nama}', nim='{self.nim}', rata={self.rata_nilai()}, status={self.status()})"


# DEMO
if __name__ == "__main__":

    print("=== FUNCTIONS ===")

    print(greet("Arifian"))
    print(tambah(5, 7))
    print(tambah(10))
    print(rata_rata([80, 90, 100]))
    print(rata_rata([]))

    print("\n=== CLASS STUDENT ===")

    # Mahasiswa 1
    mahasiswa1 = Student("Khanara", "A123")
    mahasiswa1.tambah_nilai(90)
    mahasiswa1.tambah_nilai(95)
    mahasiswa1.tambah_nilai(100)

    print(mahasiswa1)
    print("Rata-rata:", mahasiswa1.rata_nilai())
    print("Status:", mahasiswa1.status())

    # Mahasiswa 2
    mahasiswa2 = Student("Arvin", "A124")
    mahasiswa2.tambah_nilai(65)
    mahasiswa2.tambah_nilai(70)
    mahasiswa2.tambah_nilai(60)

    print(mahasiswa2)
    print("Rata-rata:", mahasiswa2.rata_nilai())
    print("Status:", mahasiswa2.status())