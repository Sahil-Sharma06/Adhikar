import React from 'react'
import {Link} from 'react-router-dom'
export default () => {
    return (
        <main className="flex flex-col items-center justify-center w-full h-screen bg-custom-dark-blue sm:px-4">
            <div className="w-full max-w-md space-y-6 text-white sm:max-w-md">
                <div className="p-4 py-6 bg-gray-800 sm:rounded-lg">
                <div className="text-center">
                    <div className="mt-5 space-y-2">
                        <h3 className="text-2xl font-bold text-white sm:text-3xl">Create an account</h3>
                        <p className="">Already have an account? <Link to="/login" className="font-medium text-custom-pink hover:text-indigo-500">
                  Log in
                </Link></p>
                    </div>
                </div>
                    <form
                        onSubmit={(e) => e.preventDefault()}
                        className="space-y-5"

                    >
                        <div>
                            <label className="font-medium">
                                Name
                            </label>
                            <input
                                type="text"
                                required
                                className="w-full px-3 py-2 mt-2 text-gray-500 bg-transparent border rounded-lg shadow-sm outline-none focus:border-indigo-600"
                            />
                        </div>
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
        </main>
    )
}