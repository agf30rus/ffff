import requests
import base64

def main():
    vmess_url = "https://raw.githubusercontent.com/Kwinshadow/TelegramV2rayCollector/main/sublinks/vmess.txt"
    vless_url = "https://raw.githubusercontent.com/Kwinshadow/TelegramV2rayCollector/main/sublinks/vless.txt"
    
    try:
        # Скачиваем свежие данные
        vmess_data = requests.get(vmess_url, timeout=15).text.strip()
        vless_data = requests.get(vless_url, timeout=15).text.strip()
        
        def get_lines(data):
            if not data:
                return []
            # Если данные в base64, декодируем их в читаемый текст
            if "://" not in data and len(data) % 4 == 0:
                try:
                    data = base64.b64decode(data).decode('utf-8', errors='ignore')
                except:
                    pass
            return [line.strip() for line in data.split('\n') if line.strip()]

        # Объединяем конфигурации в единый массив
        all_lines = get_lines(vmess_data) + get_lines(vless_data)
        merged_text = "\n".join(all_lines)
        
        # Кодируем финальный результат в Base64 для HAP Plus
        encoded_data = base64.b64encode(merged_text.encode('utf-8')).decode('utf-8')
        
        # Записываем результат в файл, который и будет нашей ссылкой подписки
        with open("subscription.txt", "w", encoding="utf-8") as f:
            f.write(encoded_data)
            
        print("Подписка успешно обновлена!")
    except Exception as e:
        print(f"Ошибка при сборке подписки: {e}")

if __name__ == "__main__":
    main()
