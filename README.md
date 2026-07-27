# 🚀 Daily C# / ASP.NET & React Q&A

Добро пожаловать в ежедневную базу знаний по **C#, ASP.NET Core и React**! 
Каждый день здесь автоматически публикуется новый разбор реального вопроса с собеседований.

---

## 📌 Вопрос Дня (День 8 — 2026-07-27)

### 🏷️ Тема: `ASP.NET Core / Security`
### ❓ Как устроена JWT (JSON Web Token) аутентификация?

#### 💡 Ответ и разбор:
JWT состоит из трех частей, разделенных точками `header.payload.signature`:

1. **Header**: тип токена (JWT) и алгоритм шифрования (например, HS256 или RS256).
2. **Payload**: утверждения (Claims) — ID пользователя, роль, имя, время истечения `exp`.
3. **Signature**: цифровая подпись, создаваемая путем хеширования (Header + Payload) с использованием секретного ключа сервера (`SecretKey`).

**Преимущества:**
* **Stateless**: Серверу не нужно хранить сессии в БД или памяти, подлинность токена проверяется математически с помощью подписи.

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

---

*Автоматически обновляется через GitHub Actions каждый день в 06:00 UTC.*
