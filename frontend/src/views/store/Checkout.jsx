import { useState, useEffect} from 'react'
import apiInstance from '../../utils/axios'
import { useParams, useNavigate } from 'react-router-dom'


function Checkout() {
    const [order, setOrder] = useState([])
    const [couponCode, setCouponCode] = useState("")
    const param = useParams()
    console.log(param)

    useEffect(() => {
        apiInstance.get(`checkout/${param.order_oid}/`).then((res) => {
            console.log(res.data)
        })
    }, [])

    const applyCoupon = async () => {
        const formdata = new FormData()
        formdata.append('order_oid', order.oid)
        formdata.append('coupon_data', couponCode)
        
        try {
            const response = await apiInstance.post('coupon/', formdata)
            console.log(response.data.message)
        } catch (error) {
            console.log(error)
        }
    }



  return (
   <main className='mb-4 mt-4'>
        <div className='container'>
            {/* SEction: Checkout form */}
            <section className=''>
                <div className='row gx-lg-5'>
                    <div className='col lg-8 mb-md-0'>
                        {/* Section: Biling Detail */}
                        <section className=''>
                            <div className='alert alert-warning'>
                                <strong>Review Your Shipping and Order Detail</strong>

                            </div>
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
                        </section>
                    </div>
                    <div className='col-lg-4 mb-4 mb-md-0'>
                        {/* Sectin Summary */}
                        <section className="shadow-4 p-4 rounded-5 mb-4">
                        <h5 className="mb-5">Order Summary</h5>
                            <div className="d-flex justify-content-between mb-3">
                                <span>Subtotal </span>
                                <span>$900</span>
                            </div>
                            <div className="d-flex justify-content-between">
                                <span>Shipping </span>
                                <span>$98</span>
                            </div>
                            <div className="d-flex justify-content-between">
                                <span>Tax </span>
                                <span>$78</span>
                            </div>
                            
                            <hr className="my-4" />
                            <div className="d-flex justify-content-between fw-bold mb-5">
                                <span>Total </span>
                                <span>${order.total}</span>
                            </div>
                            <section className='shadow rounded-3 card p-4 mb-4 rounded-5'>
                                <h5 className='mb-4'>Appl promo Code</h5>
                                <div className='d-flex align-item-center'>
                                    <input type='text'
                                        className='form-control rounded me-1'
                                        placeholder='Promo code'
                                        onChange={(e) => setCouponCode(e.target.value)}
                                    />
                                    <button type='button'
                                        className='btn btn-sucess btn-rounded overflow-visible'
                                        onClick={applyCoupon}
                                    >
                                        Apply
                                    </button>
                                </div>
                            </section>
                                
                                <button                                    
                                    className="btn btn-primary btn-rounded w-100"           
                                >
                                    Pay wih Credit Card <i className='fas fa-credit-card'></i>
                                </button>
                                
                                
                        </section>
                    </div>
                    
                </div>

            </section>
        </div>

    </main>

  )
}

export default Checkout