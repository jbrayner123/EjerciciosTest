import { render, screen, fireEvent } from '@testing-library/react'
import { test, expect } from 'vitest'
import App from './App'

test('renders title and increments counter', () => {
  render(<App />)
  expect(screen.getByText(/Hello React/i)).toBeInTheDocument()

  const button = screen.getByRole('button', { name: /count is/i })
  expect(button).toBeInTheDocument()
  fireEvent.click(button)
  expect(button.textContent).toMatch(/count is 1/i)
})
