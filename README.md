# 🚀 Daily C# / ASP.NET & React Q&A

Добро пожаловать в ежедневную базу знаний по **C#, ASP.NET Core и React**! 
Каждый день здесь автоматически публикуется новый разбор реального вопроса с собеседований.

---

## 📌 Вопрос Дня (День 21 — 2026-08-09)

### 🏷️ Тема: `C#`
### ❓ Как работают `async` и `await` под капотом в C#?

#### 💡 Ответ и разбор:
При компиляции методы с `async/await` преобразуются компилятором C# в **конечный автомат (State Machine)** на основе структуры `IAsyncStateMachine`.

**Механика работы:**
1. При встрече ключа `await` проверяется состояние задачи (`Task`). Если задача уже завершена, метод продолжается синхронно без накладных расходов.
2. Если задача не завершена, метод «замораживается», текущий контекст синхронизации сохраняется.
3. Поток высвобождается и возвращается в пуп потоков (ThreadPool) для выполнения других задач.
4. Когда асинхронная операция завершается (например, пришел ответ от сети или БД), конечный автомат восстанавливает контекст и продолжает выполнение кода после `await`.

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
| День 011 | `C#` | [Что такое Value Types (типы значений) и Reference Types (ссылочные типы)? ГДЕ они хранятся?](questions/day-011.md) |
| День 012 | `ASP.NET Core` | [Что такое SignalR и когда его следует использовать?](questions/day-012.md) |
| День 013 | `React` | [Что такое React StrictMode и почему компоненты рендерятся дважды в разработке?](questions/day-013.md) |
| День 014 | `ASP.NET Core / Architecture` | [Что такое паттерн CQRS и библиотека MediatR?](questions/day-014.md) |
| День 015 | `TypeScript` | [В чем разница между `type` и `interface` в TypeScript?](questions/day-015.md) |
| День 016 | `ASP.NET Core` | [В чем разница между Transient, Scoped и Singleton временно́й жизнью сервисов в Dependency Injection?](questions/day-016.md) |
| День 017 | `React` | [Зачем нужен хук `useEffect` и как работает его массив зависимостей?](questions/day-017.md) |
| День 018 | `C# / EF Core` | [В чем ключевая разница между `IEnumerable<T>` и `IQueryable<T>`?](questions/day-018.md) |
| День 019 | `React / TypeScript` | [Что такое Virtual DOM в React и как работает алгоритм Reconciliation (Diffing)?](questions/day-019.md) |
| День 020 | `ASP.NET Core` | [Что такое Middleware в ASP.NET Core и как работает конвейер обработки запроса (Pipeline)?](questions/day-020.md) |
| День 021 | `C#` | [Как работают `async` и `await` под капотом в C#?](questions/day-021.md) |

---

*Автоматически обновляется через GitHub Actions каждый день в 06:00 UTC.*
