import React, { useState, useEffect } from 'react'
 
import apiInstance from '../../utils/axios'
import { Link } from 'react-router-dom'

export default function Products() {

  const [products, setProducts] = useState([])
  const [category, setCategory] = useState([])
  const [colorValue, setColorValue] = useState('No Color')
  const [selectedColors, setSelectedColors] = useState({})
  const [selectedProduct, setSelectedProduct] = useState({})
  const [sizeValue, setSizeValue] = useState('No size')
  const [selectedSize, setSelectedSize] = useState({})
  const [qtyValue, setQtyValue] = useState(1)


  const handleColorButtonClick = (event, product_id, colorName) => {
    setColorValue(colorName)
    setSelectedProduct(product_id)
    setSelectedColors((preSelectedColors) => ({
      ...preSelectedColors,
      [product_id]: colorName
    }))
  }
  
  const handleSizeButtonClick = (event, product_id, sizeName) => {
    setSizeValue(sizeName)
    setSelectedProduct(product_id)

    setSelectedSize((prevSelectedSize) => ({
      ...prevSelectedSize,
      [product_id]: sizeName
    }))
  }
  const handleQtyChange = (event, product_id) => {
    setQtyValue(event.target.value)
    setSelectedProduct(product_id)
  }

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


  return (
   <>
    <main className='mt-5'>
      <div className='container'>
        <section className='text-center'>
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
        <section className='text-center'>
          <div className="row">
            {products?.map((product, index) => (
              <div className="col-lg-4 col-md-12 mb-4" key={index.id}>
                <div className="card">
                  <div
                    className="bg-image hover-zoom ripple"
                    data-mdb-ripple-color="light"
                  >
                    <Link to={`/detail/${product.slug}`}>
                      <img
                        src={product.image}
                        className="w-100"
                        style={{ width: "100px", height: "300px", objectFit: "cover" }}
                      />
                    </Link>
                  </div>
                  <div className="card-body">
                    <a href='' className='text-reset'>
                      <h5 className='card-title mb-3'>{product.title}</h5>
                    </a>
                    <a href='' className='text-reset'>
                      <p>{product.category?.title}</p>
                    </a>
                    <div className='d-flex justify-content-center'>
                      <h6 className='mb-3'>${product.price}</h6>
                      <h6 className='mb-3 text-muted ms-2'><strike>${product.price}</strike></h6>
                    </div>
                    <div className='btn-group'>
                      <button className='btn btn-primary dropdown-toggle'
                        type='button'
                        id='dropdownMenuClikable'
                        data-bs-toggle='dropdown'
                        data-bs-auto-close='false'
                        aria-expanded='false'
                      >
                        Variation
                      </button>
                      <ul className='dropdown-menu'
                        aria-labelledby='dropdownMenuClikable'

                      >
                        <div className='d-flex flex-column'>
                          <li className='p-1'>
                            <b>Quantity</b>
                          </li>
                          <div className='p-1 mt-0 pt-0 d-flex flex-wrap'>
                            <li>
                              <input className='form-control' value={qtyValue} onChange={(e) => handleQtyChange(e, product.id)} type="number" />
                            </li>
                          </div>
                        </div>
                        {product.size?.length > 0 &&
                          <div className='d-flex flex-column'>
                            <li className='p-1'>
                              <b>Size</b>: {selectedSize[product.id] || 'Select a Size'}
                            </li>
                            <div className='p-1 mt-0 pt-0 d-flex flex-wrap'>
                              {product.size?.map((s, index) => (
                                <li>
                                  <button onClick={(e) => handleSizeButtonClick(e, product.id, s.name)} 
                                    className='btn btn-secondary btn-sm me-2 mb-1'>
                                    XXL
                                  </button>
                                </li>
                              ))}

                            </div>

                          </div> 
                        
                        }
                        {product.color?.length > 0 &&
                          <div className='d-flex flex-column mt-3'>
                            <li className='p-1'>
                              <b>Color</b>:{selectedColors[product.id] || 'Select a Color'}
                            </li>
                            <div className='p-1 mt-0 pt-0 d-flex flex-wrap'>
                              {product.color?.map((c, index) => (
                                <li>
                                  <button
                                    className='btn btn-sm me-2 mb-1 p-3'
                                    style={{ backgroundColor: `${c.color_code}`}}
                                    onClick={(e) => handleColorButtonClick(e, product.id, c.name)}
                                  />
                                </li>
                              ))}
                            </div>
                            
                          </div>
                        }
                  

                      </ul>

                    </div>
                   
                    <button
                      type='button'
                      className='btn btn-primary px-3 ms-2'
                    >
                      <i className='fas fa-shopping-cart' />
                    </button>                                         
                    <button
                          
                          type="button"
                          className="btn btn-danger px-3 ms-2 "
                         >
                          <i className="fas fa-heart" />
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
