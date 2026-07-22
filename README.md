# 🚀 Daily C# / ASP.NET & React Q&A

Добро пожаловать в ежедневную базу знаний по **C#, ASP.NET Core и React**! 
Каждый день здесь автоматически публикуется новый разбор реального вопроса с собеседований.

---

## 📌 Вопрос Дня (День 3 — 2026-07-22)

### 🏷️ Тема: `C# / EF Core`
### ❓ В чем ключевая разница между `IEnumerable<T>` и `IQueryable<T>`?

#### 💡 Ответ и разбор:
Главное отличие заключается в **месте выполнения запроса** и способе его трансляции:

1. **`IEnumerable<T>` (LINQ to Objects)**:
   * Фильтрация происходит в **памяти приложения** (.NET CLR).
   * Выполняет SQL-запрос к БД и вытягивает **все** записи в память, а затем фильтрует их.

2. **`IQueryable<T>` (LINQ to Entities)**:
   * Наследует `IEnumerable`, но содержит `Expression Tree` (дерево выражений).
   * Фильтрация происходит **на стороне СУБД**.
   * EF Core транслирует выражения в оптимальный SQL-запрос (`WHERE`, `TOP`, `JOIN`) и запрашивает из БД только нужные строки.

```csharp
// IQueryable: в БД уходит `SELECT * FROM Users WHERE Age > 18`
IQueryable<User> query = dbContext.Users.Where(u => u.Age > 18);

// IEnumerable: в БД уходит `SELECT * FROM Users`, фильтрация идет в C#
IEnumerable<User> list = dbContext.Users.AsEnumerable().Where(u => u.Age > 18);
```

---

## 📚 Архив пройденных вопросов

| День | Тема | Вопрос |
|---|---|---|
| День 001 | `ASP.NET Core` | [В чем разница между Transient, Scoped и Singleton временно́й жизнью сервисов в Dependency Injection?](questions/day-001.md) |
| День 002 | `React` | [Зачем нужен хук `useEffect` и как работает его массив зависимостей?](questions/day-002.md) |
| День 003 | `C# / EF Core` | [В чем ключевая разница между `IEnumerable<T>` и `IQueryable<T>`?](questions/day-003.md) |

---

*Автоматически обновляется через GitHub Actions каждый день в 06:00 UTC.*
