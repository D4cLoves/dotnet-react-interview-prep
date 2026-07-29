# 🚀 Daily C# / ASP.NET & React Q&A

Добро пожаловать в ежедневную базу знаний по **C#, ASP.NET Core и React**! 
Каждый день здесь автоматически публикуется новый разбор реального вопроса с собеседований.

---

## 📌 Вопрос Дня (День 10 — 2026-07-29)

### 🏷️ Тема: `React / State`
### ❓ В чем разница между Redux Toolkit, TanStack Query (React Query) и Zustand?

#### 💡 Ответ и разбор:
Они решают разные задачи менеджмента состояния:

1. **TanStack Query (React Query)**:
   * Специализирован для **Server State** (асинхронные данные с API).
   * Автоматически кэширует, обновляет в фоновом режиме (stale-while-revalidate), обрабатывает загрузку и ошибки.

2. **Redux Toolkit**:
   * Глобальное **Client State** с единственным хранилищем (Single Source of Truth).
   * Подходит для огромных корпоративных приложений со сложной логикой клиента.

3. **Zustand**:
   * Минималистичный и быстрый менеджер глобального состояния без лишнего шаблонного кода (boilerplate).
   * Идеален как легкая альтернатива Redux.

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
| День 010 | `React / State` | [В чем разница между Redux Toolkit, TanStack Query (React Query) и Zustand?](questions/day-010.md) |

---

*Автоматически обновляется через GitHub Actions каждый день в 06:00 UTC.*
