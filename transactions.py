import subprocess

def save_output_to_file(output):
    with open("SignatureRSZ.txt", "a") as file:
        file.write(output)

# Number of signatures in a Bitcoin transaction
for i in range(32):
    process = subprocess.run(
        ["./darksignature", "-pubkey",
         "ca5606a1e820e7a2f6bb3ab090e8ade7b04a7e0b5909a68dda2744ae3b8ecbfa",
         "280a47639c811134d648e8ee8096c33b41611be509ebca837fbda10baaa1eb15"],
        stdout=subprocess.PIPE,
        universal_newlines=True
    )

    output = f"|ECDSA Signature R,S,Z values from Bitcoin №{i+1}:\n{process.stdout}\n"
    print(output)
    save_output_to_file(output)
