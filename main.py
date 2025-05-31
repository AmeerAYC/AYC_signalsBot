from send_to_telegram import send_message

def main():
    # مثال على توصية وهمية
    recommendation = "🔔 توصية جديدة
الدخول: 1.2345
الهدف: 1.2450
الستوب: 1.2280"
    send_message(recommendation)

if __name__ == "__main__":
    main()