import { render, screen, fireEvent } from '@testing-library/react'
import { vi, test, expect } from 'vitest'
import LoginForm from './LoginForm'

test('submits email and password', () => {
  const onSubmit = vi.fn()
  render(<LoginForm onSubmit={onSubmit} />)

  // Make sure your <form> has aria-label="login-form"
  fireEvent.change(screen.getByLabelText(/email/i), { target: { value: 'a@b.com' } })
  fireEvent.change(screen.getByLabelText(/password/i), { target: { value: 'secret' } })

  fireEvent.submit(screen.getByRole('form', { name: /login-form/i }))

  expect(onSubmit).toHaveBeenCalledTimes(1)
  expect(onSubmit).toHaveBeenCalledWith({ email: 'a@b.com', password: 'secret' })
})