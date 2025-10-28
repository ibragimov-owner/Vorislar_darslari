# Rainbow ASCII loader (terminalda slow animatsiya) — oddiy va ko‘zga yoqadi.

# rainbow_loader.py

# Kod quyidagicha:
import sys, time, itertools

frames = ['⠋','⠙','⠹','⠸','⠼','⠴','⠦','⠧','⠇','⠏']
msg = " yuklanmoqda... "

try:
    for i in itertools.cycle(range(len(frames))):
        frame = frames[i % len(frames)]
        bar = (i % 20) * "█" + (20 - (i % 20)) * " "
        sys.stdout.write(f"\r{frame} [{bar}] {msg}{(i%100):02d}%")
        sys.stdout.flush()
        time.sleep(0.08)
except KeyboardInterrupt:
    sys.stdout.write("\r✅ Yuklash tugadi!                     \n")