import React from 'react'
import { useAuthStore } from '../../store/auth'
import { Link } from 'react-router-dom'


export default function Dashboard() {
    const [isLoggedIn, setIsLoading] = useAuthStore((state) => {
        state.isLoggedIn,
        state.user

    })
    

    return (
    <div>
      <h1>Home Dashboard</h1>
    </div>
  )
}
