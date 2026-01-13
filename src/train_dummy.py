import time

def train():
    print("Starting dummy training...")
    loss = 1.0
    for epoch in range(1, 6):
        loss *= 0.7
        print(f"Epoch {epoch}: loss={loss:.4f}")
        time.sleep(0.2)
    print("Training done.")

if __name__ == "__main__":
    train()
