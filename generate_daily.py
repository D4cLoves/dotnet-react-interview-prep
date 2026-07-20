import json
import os
import sys
from datetime import datetime

# Set UTF-8 encoding for standard output on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def main():
    questions_file = 'questions.json'
    counter_file = 'current_day.txt'
    questions_dir = 'questions'

    if not os.path.exists(questions_file):
        print(f"Error: {questions_file} not found.")
        return

    with open(questions_file, 'r', encoding='utf-8') as f:
        questions = json.load(f)

    if not questions:
        print("Error: No questions found in questions.json.")
        return

    # Read current day index
    day_idx = 0
    if os.path.exists(counter_file):
        with open(counter_file, 'r', encoding='utf-8') as f:
            try:
                day_idx = int(f.read().strip())
            except ValueError:
                day_idx = 0

    current_q = questions[day_idx % len(questions)]
    day_number = day_idx + 1
    today_str = datetime.now().strftime('%Y-%m-%d')

    # Ensure questions directory exists
    os.makedirs(questions_dir, exist_ok=True)

    # Save individual day markdown file
    day_filename = f"{questions_dir}/day-{day_number:03d}.md"
    day_content = f"""# Day {day_number} ({today_str}): [{current_q['topic']}] {current_q['question']}

### ❓ Вопрос:
{current_q['question']}

### 💡 Ответ:
{current_q['answer']}
"""
    with open(day_filename, 'w', encoding='utf-8') as f:
        f.write(day_content)

    # Generate table of published days
    archive_lines = []
    for d in range(1, day_number + 1):
        q_item = questions[(d - 1) % len(questions)]
        archive_lines.append(f"| День {d:03d} | `{q_item['topic']}` | [{q_item['question']}](questions/day-{d:03d}.md) |")

    archive_table = "\n".join(archive_lines)

    # Write main README.md
    readme_content = f"""# 🚀 Daily C# / ASP.NET & React Q&A

Добро пожаловать в ежедневную базу знаний по **C#, ASP.NET Core и React**! 
Каждый день здесь автоматически публикуется новый разбор реального вопроса с собеседований.

---

## 📌 Вопрос Дня (День {day_number} — {today_str})

### 🏷️ Тема: `{current_q['topic']}`
### ❓ {current_q['question']}

#### 💡 Ответ и разбор:
{current_q['answer']}

---

## 📚 Архив пройденных вопросов

| День | Тема | Вопрос |
|---|---|---|
{archive_table}

---

*Автоматически обновляется через GitHub Actions каждый день в 06:00 UTC.*
"""

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

    # Save next day index
    with open(counter_file, 'w', encoding='utf-8') as f:
        f.write(str(day_number))

    print(f"Successfully generated Day {day_number}: {current_q['question']}")

if __name__ == '__main__':
    main()

