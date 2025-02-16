import React, { useState, useEffect } from 'react'
 
import apiInstance from '../../utils/axios'

export default function Products() {

  const [products, setProducts] = useState([])

  useEffect(() => {
    apiInstance.get(`products/`).then((response) => {
      setProducts(response.data)

    })
  })
  console.log(products)

  return (
    <div>
      
    </div>
  )
}
