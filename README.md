# 🚀 Daily C# / ASP.NET & React Q&A

Добро пожаловать в ежедневную базу знаний по **C#, ASP.NET Core и React**! 
Каждый день здесь автоматически публикуется новый разбор реального вопроса с собеседований.

---

## 📌 Вопрос Дня (День 5 — 2026-07-24)

### 🏷️ Тема: `ASP.NET Core`
### ❓ Что такое Middleware в ASP.NET Core и как работает конвейер обработки запроса (Pipeline)?

#### 💡 Ответ и разбор:
Middleware — это программный компонент, встраиваемый в конвейер (pipeline) приложения для обработки HTTP-запросов и ответов.

**Принцип работы (цепочка вызовов):**
Каждый Middleware компонент:
1. Получает HTTP-контекст (`HttpContext`).
2. Может выполнить код **до** передачи управления следующему Middleware.
3. Вызывает `next.Invoke()` для передачи управления дальше по цепочке.
4. Может выполнить код **после** возврата управления от следующего Middleware.
5. Может прервать цепочку (Short-circuit), например, если пользователь не авторизован.

```csharp
app.Use(async (context, next) =>
{
    // Логика ДО следующего middleware
    Console.WriteLine("Request In");
    await next.Invoke();
    // Логика ПОСЛЕ следующего middleware
    Console.WriteLine("Response Out");
});
```

---

## 📚 Архив пройденных вопросов

| День | Тема | Вопрос |
|---|---|---|
| День 001 | `ASP.NET Core` | [В чем разница между Transient, Scoped и Singleton временно́й жизнью сервисов в Dependency Injection?](questions/day-001.md) |
| День 002 | `React` | [Зачем нужен хук `useEffect` и как работает его массив зависимостей?](questions/day-002.md) |
| День 003 | `C# / EF Core` | [В чем ключевая разница между `IEnumerable<T>` и `IQueryable<T>`?](questions/day-003.md) |
| День 004 | `React / TypeScript` | [Что такое Virtual DOM в React и как работает алгоритм Reconciliation (Diffing)?](questions/day-004.md) |
| День 005 | `ASP.NET Core` | [Что такое Middleware в ASP.NET Core и как работает конвейер обработки запроса (Pipeline)?](questions/day-005.md) |

---

*Автоматически обновляется через GitHub Actions каждый день в 06:00 UTC.*
