import React from 'react'
import { Link } from 'react-router-dom'

const Login = () => {
  return (
    <div className="flex items-center justify-center h-screen text-white bg-custom-dark-blue">
      <div className="w-full max-w-md p-8 bg-gray-800 rounded-lg shadow-lg">
        <h1 className="mb-2 text-3xl font-bold text-center">Login</h1>

        <div className="flex flex-col items-center mb-4">
          <p className="text-center">
            Don't have an account?{' '}
            <Link
              to="/register"
              className="font-medium text-custom-pink hover:text-indigo-500"
            >
              Sign Up
            </Link>
          </p>
        </div>

        <form
                        onSubmit={(e) => e.preventDefault()}
                        className="space-y-5"

                    >
                        <div>
                            <label className="font-medium">
                                Email
                            </label>
                            <input
                                type="email"
                                required
                                className="w-full px-3 py-2 mt-2 text-gray-500 bg-transparent border rounded-lg shadow-sm outline-none focus:border-indigo-600"
                            />
                        </div>
                        <div>
                            <label className="font-medium">
                                Password
                            </label>
                            <input
                                type="password"
                                required
                                className="w-full px-3 py-2 mt-2 text-gray-500 bg-transparent border rounded-lg shadow-sm outline-none focus:border-indigo-600"
                            />
                        </div>
                        <button
                            className="w-full px-4 py-2 font-medium text-white duration-150 rounded-lg bg-custom-pink hover:bg-indigo-500 active:bg-indigo-600"
                        >
                            Create account
                        </button>
                    </form>
      </div>
    </div>
  )
}

export default Login
