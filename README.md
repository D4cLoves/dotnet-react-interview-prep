# 🚀 Daily C# / ASP.NET & React Q&A

Добро пожаловать в ежедневную базу знаний по **C#, ASP.NET Core и React**! 
Каждый день здесь автоматически публикуется новый разбор реального вопроса с собеседований.

---

## 📌 Вопрос Дня (День 9 — 2026-07-28)

### 🏷️ Тема: `EF Core`
### ❓ Что такое проблема N+1 запросов в EF Core и как её избежать?

#### 💡 Ответ и разбор:
Проблема N+1 возникает при обращении к связанным сущностям в цикле, когда EF Core делает 1 запрос для получения списка главных сущностей и по N запросов для каждого связанного элемента.

**Решения:**
1. **Eager Loading (Жадная загрузка)**: Использовать `.Include()` и `.ThenInclude()`. Все данные подтянутся за 1 SQL-запрос с `JOIN`.
2. **Explicit Loading**: Загружать связи явно через `dbContext.Entry(user).Collection(...).Load()`.
3. **Projection**: Проектировать сразу в DTO через `.Select()`, выбирая только нужные поля.

---

## 📚 Архив пройденных вопросов

| День | Тема | Вопрос |
|---|---|---|
| День 001 | `ASP.NET Core` | [В чем разница между Transient, Scoped и Singleton временно́й жизнью сервисов в Dependency Injection?](questions/day-001.md) |
| День 002 | `React` | [Зачем нужен хук `useEffect` и как работает его массив зависимостей?](questions/day-002.md) |
| День 003 | `C# / EF Core` | [В чем ключевая разница между `IEnumerable<T>` и `IQueryable<T>`?](questions/day-003.md) |
| День 004 | `React / TypeScript` | [Что такое Virtual DOM в React и как работает алгоритм Reconciliation (Diffing)?](questions/day-004.md) |
| День 005 | `ASP.NET Core` | [Что такое Middleware в ASP.NET Core и как работает конвейер обработки запроса (Pipeline)?](questions/day-005.md) |
| День 006 | `C#` | [Как работают `async` и `await` под капотом в C#?](questions/day-006.md) |
| День 007 | `React` | [В чем разница между `useMemo` и `useCallback`?](questions/day-007.md) |
| День 008 | `ASP.NET Core / Security` | [Как устроена JWT (JSON Web Token) аутентификация?](questions/day-008.md) |
| День 009 | `EF Core` | [Что такое проблема N+1 запросов в EF Core и как её избежать?](questions/day-009.md) |

---

*Автоматически обновляется через GitHub Actions каждый день в 06:00 UTC.*
