import subprocess

def save_output_to_file(output):
    with open("SignatureRSZ.txt", "a") as file:
        file.write(output)

# Number of signatures in a Bitcoin transaction
for i in range(32):
    process = subprocess.run(
        ["./darksignature", "-pubkey",
         "9b4069d8237fae8f2417c71c5512ec1b0547b5597474480cc28ea1bbfeecaab8",
         "b90fdec161ad6ef4378f274a60b900452431533596bf3bd23e01202ebf679461"],
        stdout=subprocess.PIPE,
        universal_newlines=True
    )

    output = f"|ECDSA Signature R,S,Z values from Bitcoin №{i+1}:\n{process.stdout}\n"
    print(output)
    save_output_to_file(output)