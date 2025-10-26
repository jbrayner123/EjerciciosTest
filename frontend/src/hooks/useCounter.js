import { useState } from 'react'

export function useCounter(initial = 0) {
  const [count, setCount] = useState(initial)

  const inc = (step = 1) => {
    setCount(prev => prev + step)
  }

  const dec = (step = 1) => {
    setCount(prev => prev - step)
  }

  const reset = () => {
    setCount(initial)
  }

  return { count, inc, dec, reset }
}