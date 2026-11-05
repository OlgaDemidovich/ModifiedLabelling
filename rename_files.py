from pathlib import Path
from PIL import Image

# === ПУТИ ===
IMG_DIR = Path(r"potholes_400")
LBL_DIR = Path(r"potholes_labels")
PREFIX="web_"

# Расширения изображений для обработки
IMG_EXTS = (".jpg", ".jpeg", ".png", ".webp")

# Собираем список всех изображений
images = []
for f in IMG_DIR.iterdir():
    if f.is_file() and f.suffix.lower() in IMG_EXTS:
        images.append(f)

# Сортируем по имени, чтобы нумерация была предсказуемой
images.sort(key=lambda x: x.name.lower())

if not images:
    print("Изображений не найдено. Проверь путь IMG_DIR")
    raise SystemExit

print(f"Найдено изображений: {len(images)}")
print("Старт обработки...")
print("-" * 40)

processed = 0

for idx, img_path in enumerate(images, start=1):
    old_stem = img_path.stem
    new_stem = f"{PREFIX}{idx}"

    new_img_path = IMG_DIR / f"{new_stem}.jpg"
    old_txt_path = LBL_DIR / f"{old_stem}.txt"
    new_txt_path = LBL_DIR / f"{new_stem}.txt"

    # Конвертируем/пересохраняем изображение в JPG
    try:
        with Image.open(img_path) as im:
            # Переводим в RGB, убираем альфа-канал если есть
            im = im.convert("RGB")
            im.save(new_img_path, "JPEG", quality=95)
        print(f"[IMG] {img_path.name} -> {new_img_path.name}")
    except Exception as e:
        print(f"[ERR] Не удалось обработать изображение {img_path.name}: {e}")
        continue

    # Переименовываем соответствующий txt в той же нумерации
    if old_txt_path.exists():
        try:
            old_txt_path.rename(new_txt_path)
            print(f"[TXT] {old_txt_path.name} -> {new_txt_path.name}")
        except Exception as e:
            print(f"[ERR] Не удалось переименовать {old_txt_path.name}: {e}")
    else:
        print(f"[WARN] Не найден {old_stem}.txt в {LBL_DIR}")

    # Удаляем старый файл изображения
    if img_path.resolve() != new_img_path.resolve():
        try:
            img_path.unlink()
            print(f"[DEL] Удалён {img_path.name}")
        except Exception as e:
            print(f"[ERR] Не удалось удалить {img_path.name}: {e}")

    processed += 1

print("-" * 40)
print(f"Готово. Обработано: {processed}")
print(f"В {IMG_DIR} остались только {PREFIX}1.jpg ... {PREFIX}{processed}.jpg")
print(f"В {LBL_DIR} остались только {PREFIX}1.txt ... {PREFIX}{processed}.txt")