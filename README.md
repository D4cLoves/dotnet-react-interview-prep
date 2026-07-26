# 🚀 Daily C# / ASP.NET & React Q&A

Добро пожаловать в ежедневную базу знаний по **C#, ASP.NET Core и React**! 
Каждый день здесь автоматически публикуется новый разбор реального вопроса с собеседований.

---

## 📌 Вопрос Дня (День 7 — 2026-07-26)

### 🏷️ Тема: `React`
### ❓ В чем разница между `useMemo` и `useCallback`?

#### 💡 Ответ и разбор:
Оба хука используются для оптимизации производительности за счет **мемоизации**:

1. **`useMemo`**:
   * Кэширует **результат вычислений** функции.
   * Перевычисляет значение только при изменении зависимостей.
   * Используется для тяжелых расчетов.

2. **`useCallback`**:
   * Кэширует **саму ссылку на функцию** между рендерами.
   * Используется при передаче дочерним компонентам колбэков, чтобы избежать лишних перерендеров этих компонентов.

```tsx
// useMemo хранит значение (число, массив, объект)
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);

// useCallback хранит ссылку на функцию
const memoizedCallback = useCallback(() => {
  doSomething(a, b);
}, [a, b]);
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
| День 006 | `C#` | [Как работают `async` и `await` под капотом в C#?](questions/day-006.md) |
| День 007 | `React` | [В чем разница между `useMemo` и `useCallback`?](questions/day-007.md) |

---

*Автоматически обновляется через GitHub Actions каждый день в 06:00 UTC.*
