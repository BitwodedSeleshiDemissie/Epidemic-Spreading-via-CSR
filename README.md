# ✈️ CSR Epidemic Spread via Air Travel 🌍  
![Epidemic Simulation](figures/infections.gif)  

What happens if an epidemic starts at one airport? How fast can it spread globally through flights?  
This project models epidemic dynamics using **sparse matrix–vector multiplication in CSR (Compressed Sparse Row) format**, applied to the **OpenFlights airline network**.  

---

## 🚀 Why This Project  

Air traffic networks are massive, with thousands of airports and tens of thousands of routes — but very **sparse** (most airports don’t connect directly).  
CSR representation allows us to simulate global spread **efficiently** with matrix × vector operations, instead of brute-force graph traversal.  

This project demonstrates:  
- Sparse linear algebra in action  
- A real-world dataset (OpenFlights)  
- Visual and animated epidemic simulations  

---

## 📊 How It Works  

1. **Data**  
   - Airports → graph nodes  
   - Routes → graph edges  
   - Stored as a CSR adjacency matrix  

2. **Simulation**  
   - Start with one infected airport (e.g., Hong Kong or JFK)  
   - Multiply adjacency matrix × infection vector  
   - Each multiplication = one “hop” of the epidemic  

3. **Output**  
   - Infection counts per step  
   - Static plots of infected airports  
   - Animated `.gif` of infection spreading across the world  

---

## 🛠️ Installation  

```bash
git clone https://github.com/<your-username>/csr-epidemic-spread.git
cd csr-epidemic-spread

python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt


## This project also helps in the process of public policy planning to take into account how fast such a scenario could become a global concern within a short amount of time. 
