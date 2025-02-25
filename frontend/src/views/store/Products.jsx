import React, { useState, useEffect } from 'react'
 
import apiInstance from '../../utils/axios'
import { Link } from 'react-router-dom'

export default function Products() {

  const [products, setProducts] = useState([])
  const [category, setCategory] = useState([])

  useEffect(() => {
    apiInstance.get(`/category`).then((res) => {
      setCategory(res.data)
    })
  }, [])
  useEffect(() => {
    apiInstance.get(`products/`).then((res) => {
      setProducts(res.data)

    })
  }, [])

  const itemsPerPage = 6 // items to be display per page
  const [currentPage, setCurrentPage] = useState(1) // manage the current page display

  // Calculate the index of the last item on the current page
  const indexOfLastItem = currentPage * itemsPerPage;

  // Calculate the index of the first item on the current page
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;
  const currentItems = products.slice(indexOfFirstItem, indexOfLastItem);
  const selectedProduct = null  


  return (
   <>
    <main className='mt-5'>
      <div className='container'>
        <section className='text-center container'>
          <div className='row mt-4 mb-3'>
            <div className='col-lg-6 col-md-8 mx-auto'>
              <h1 className="fw-light">Hot Category🔥</h1>
                <p className="lead text-muted">
                    Our Latest Categories
              </p>
            </div> 
          </div>
        </section>
        <div className='d-flex justify-content-center'>
          {category.map((c, index) => (
            <div className='align-items-center d-flex flex-column' style={{ background: '#e8e8e8', marginLeft: '10px', borderRadius: '10px', padding: '30px' }}>
              <Link>
                <img src={c.image} alt=""
                  style={{ width: '180px', height: '180px', objectFit: 'cover' }}
                />
              </Link>
              <p><a href='' className='text-dark'>{c.title}</a>  </p>
            </div>

          ))}
        </div>
        <section className="text-center container">
          <div className="row mt-4 mb-3">
            <div className="col-lg-6 col-md-8 mx-auto">
              <h1 className="fw-light">Featured Products 📍</h1>
              <p className="lead text-muted">
                  Our Featured Products
              </p>
            </div>
          </div>
        </section>
        <section className='text-cententer'>
          <div className='row'>
            {currentItems.map((product, index) => (
              <div className='col-lg-4 col-md-12 mb-4' key={index.id}>
                <div className='bg-image hover-zoom ripple'
                  data-mdb-ripple-color='light'
                >
                  <Link to={`/detail/${product.slug}/`}>
                    <img src={(selectedProduct === product.id && colorImage) ? colorImage : product.image} 
                      alt="" className='w-100'
                      style={{ width: '100px', height: '300px', objectFit: 'cover'}}
                     />
                  </Link>                  
                </div>
                <div className='card-body'>
                  <a href='' className='text-body justify-content-center'>
                    <h5 className='card-title mb-3'>{product.title}</h5>
                  </a>
                  <a href='' className='text-reset justify-content-center'>
                    <p>{product.category?.title}</p>

                  </a>
                  <div className='d-flex '>
                    <h6 className='mb-3'>${product.price}</h6> 

                  </div>
                  <div className='btn-group justify-content-center' >
                    <button className='btn btn-primary dropdown-toggle' type='button'
                      id='dropdownMenuClickable'
                      data-bs-toggle='dropdown'
                      data-bs-auto-close='false'
                      aria-expanded='false'
                    >
                      Variation
                    </button>
                  </div>
                </div>

                

              </div>
            ))}

          </div>

        </section>
      </div>

    </main>
   
   </>
    
  )
}
