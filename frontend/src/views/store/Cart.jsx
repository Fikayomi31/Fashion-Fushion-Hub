import React, { useEffect, useState } from 'react'
import apiInstance from '../../utils/axios'
import UserData from '../plugin/UserData'
import CardID from '../plugin/CardID'


function Cart() {
  const [cart, setCart] = useState([])
  const [cartTotal, setCartTotal] = useState([])
  const [productQuantities, setProductQuantities] = useState('')

  const userData = UserData()
  const cart_id = CardID()


  const fetchCartData = (cartId, userId) => {
    const url = userId ? `cart-list/${cartId}/${userId}/` : `cart-list/${cartId}/`
    apiInstance.get(url).then((res) => {
        setCart(res.data)

    })
  }

  const fetchCartTotal = (cartId, userId) => {
    const url = userId ? `cart-detail/${cartId}/${userId}/` : `cart-detail/${cartId}/`
    apiInstance.get(url).then((res) => {
        setCartTotal(res.data)

    })
  }

  if (cart_id !== null || cart_id !== undefined) {
    if (userData !== undefined) {
        // Send Cart Data with userId and cartId
        useEffect(() => {
            fetchCartData(cart_id, userData?.user_id)
            fetchCartTotal(cart_id, userData?.user_id)

        }, [])
    } else {
        // Send cart data with 
        useEffect(() => {
            fetchCartData(cart_id, null)
            fetchCartTotal(cart_id, null)
        }, [])

    }
  }
  useEffect(() => {
    const initialQuantities = {}
    cart.forEach((c) => {
        initialQuantities[c.product?.id] = c.qty
    })
    setProductQuantities(initialQuantities)
  }, [cart])

  const handleQtyChange = (event, product_id) => {
    const quantity = event.target.value

    setProductQuantities((preQunatities) => ({
        ...preQunatities,
        [product_id]:quantity
    }))
  }
 
  return (
    <div>
      <main className='mt-6'>
        <div className='container'>
          {/* Main layout */}
          <main className='mb-6'>
            <div className='container'>
              {/* Section Cart */}
              <section className=''>
                <div className='row gx-lg-5'>
                  <div className='col-lg-8 mb-4 mb-md-0'>
                    {/* Section Product List */}
                    <section className='mb-5'>
                      {cart?.map((c, index) => (
                        <div className='row border-bottom mb-4' key={index}>
                            <div className='col-md-2 mb-4 mb-md-0'>
                            <div className='bg-image ripple rounded-5 mb-4 overflow-hidden d-block'
                                data-ripple-color='light'
                            >
                                <img
                                src={c.product?.image} 
                                className='w-100'
                                alt='big image'
                                style={{ width: '100%', height: "100px", objectFit: "cover", borderRadius: "10px" }}
                                />
                                <a href="#!">
                                <div className="hover-overlay">
                                    <div
                                    className="mask"
                                    style={{ backgroundColor: "hsla(0, 0%, 98.4%, 0.2)" }}
                                    />
                                </div>
                                </a>
                            </div>
                            </div>
                            <div className='col-md-8 mb-4 mb-md-0'>
                                <p className='fw-bold'>{c.product?.title}</p>
                                <p className='mb-1'>
                                    <span className='text-muted me-2'>Price:</span>
                                    <span>${c.price}</span>
                                </p>
                                {c.size !== "No Size" &&
                                    <p className='mb-1'>
                                        <span className='text-muted me-2'>Size</span>
                                        <span>{c.size}</span>
                                    </p>
                                }
                                {c.color !== "No Color" && 
                                    <p>
                                        <span className='text-muted me-2'>Color:</span>
                                        <span>{c.color}</span>
                                    </p>
                                }
                                <p className='mb-4'>
                                    <a href='' className='text-danger pe-3 border-end'>
                                        <small>
                                            <i className='fas fa-trash me-2'/>
                                            Remove
                                        </small>
                                    </a>
                                    <a href='' className='text-muted ps-3'>
                                        <small>
                                            <i className='fas fa-heart me-2'/>
                                            Move to wishlist
                                        </small>
                                    </a>
                                </p>
                            </div>
                            <div className='col-md-2 mb-4 mb-md-0'>
                                <div className='form-outline d-flex mb-4'>
                                    
                                    <input type='number'
                                        id='typeNumber'
                                        className='form-control'
                                        defaultValue={1}
                                        value={productQuantities[c.product?.id] || c.qty}
                                        min={1}
                                        onChange={(e) => handleQtyChange(e, c.product_id)}
                                    />
                                    <button className='btn btn-primary ms-2'><i className='fas fa-rotate-right'></i></button>
                                    
                                </div>
                                <h5 className='mb-2'>
                                    <p>Sub Total</p>
                                    <s className='text-muted me-2 small align-middle'>
                                       ${c.sub_total}
                                    </s>
                                    
                                </h5>
                               
                            </div>
                        </div>
                      ))}

                      {cart.length < 1 &&
                        <h4>Your Cart is Empty</h4>
                      
                      }
                      
                    </section>
                    {cart?.length > 0 &&                    
                        <form>
                            <h5 className="mb-4 mt-4">Contact Information</h5>
                            {/* 2 column grid layout with text inputs for the first and last names */}
                            <div className='row mb-4'>
                                <div className='col'>
                                    <div className='form-outline'>
                                    <label className="form-label" htmlFor="full_name"> <i className='fas fa-user'></i> Full Name</label>
                                    <input 
                                        type="text"
                                        id=""
                                        name='fullName'
                                        className="form-control"
                                    />
                                    </div>
                                </div>
                            </div>
                            <div className="row mb-4">
                                <div className="col">
                                    <div className="form-outline">
                                        <label className="form-label" htmlFor="form6Example1"><i className='fas fa-envelope'></i> Email</label>
                                            <input
                                                type="text"
                                                id="form6Example1"
                                                className="form-control"
                                                name='email'
                                                
                                            />
                                    </div>
                                </div>
                                <div className="col">
                                    <div className="form-outline">
                                        <label className="form-label" htmlFor="form6Example1"><i className='fas fa-phone'></i> Mobile</label>
                                            <input
                                                type="text"
                                                id="form6Example1"
                                                className="form-control"
                                                name='mobile'
                                            />
                                    </div>
                                </div>
                            </div>
                            <h5 className="mb-1 mt-4">Shipping address</h5>

                            <div className="row mb-4">
                                <div className="col-lg-6 mt-3">
                                    <div className="form-outline">
                                        <label className="form-label" htmlFor="form6Example1"> Address</label>
                                            <input
                                                type="text"
                                                id="form6Example1"
                                                className="form-control"
                                                name='address'
                                            />
                                    </div>
                                </div>
                                <div className="col-lg-6 mt-3">
                                    <div className="form-outline">
                                        <label className="form-label" htmlFor="form6Example1"> City</label>
                                            <input
                                                type="text"
                                                id="form6Example1"
                                                className="form-control"
                                                name='city'
                                            />
                                    </div>
                                </div>

                                <div className="col-lg-6 mt-3">
                                    <div className="form-outline">
                                        <label className="form-label" htmlFor="form6Example1"> State</label>
                                            <input
                                                type="text"
                                                id="form6Example1"
                                                className="form-control"
                                                name='state'
                                            />
                                    </div>
                                </div>
                                <div className="col-lg-6 mt-3">
                                    <div className="form-outline">
                                        <label className="form-label" htmlFor="form6Example1"> Country</label>
                                            <input
                                                type="text"
                                                id="form6Example1"
                                                className="form-control"
                                                name='country'
                                            
                                            />
                                    </div>
                                </div>
                            </div>

                        </form>
                    }
                  </div>
                  <div className="col-lg-4 mb-4 mb-md-0">
                    {/* Section: Summary */}
                    <section className="shadow-4 p-4 rounded-5 mb-4">
                    <h5 className="mb-5">Cart Summary</h5>
                        <div className="d-flex justify-content-between mb-3">
                            <span>Subtotal </span>
                            <span>${cartTotal.sub_total?.toFixed(2)}</span>
                        </div>
                        <div className="d-flex justify-content-between">
                            <span>Shipping </span>
                            <span>${cartTotal.shipping?.toFixed(2)}</span>
                        </div>
                        <div className="d-flex justify-content-between">
                            <span>Tax </span>
                            <span>${cartTotal.tax?.toFixed(2)}</span>
                        </div>
                        
                        <hr className="my-4" />
                        <div className="d-flex justify-content-between fw-bold mb-5">
                            <span>Total </span>
                            <span>${cartTotal.total?.toFixed(2)}</span>
                        </div>
                            
                            <button
                                
                                className="btn btn-primary btn-rounded w-100"
                            >
                                Got to checkout
                            </button>
                            
                    </section>
                </div>
                </div>

              </section>
            </div>
          </main>
        </div>
      </main>
      
    </div>
  )
}

export default Cart