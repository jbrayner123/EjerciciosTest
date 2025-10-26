import { renderHook, act } from '@testing-library/react'
import { test, expect } from 'vitest'
import { useCounter } from './useCounter'

test.skip('initial state', () => {
  const { result } = renderHook(() => useCounter(5))
  expect(result.current.count).toBe(5)
})

test.skip('inc, dec, reset', () => {
  const { result } = renderHook(() => useCounter(2))
  act(() => result.current.inc())
  expect(result.current.count).toBe(3)
  act(() => result.current.inc(2))
  expect(result.current.count).toBe(5)
  act(() => result.current.dec())
  expect(result.current.count).toBe(4)
  act(() => result.current.reset())
  expect(result.current.count).toBe(2)
})
