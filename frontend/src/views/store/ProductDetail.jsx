import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import apiInstance from '../../utils/axios'
import Products from './Products'
import UserData from '../plugin/UserData'
import CardID from '../plugin/CardID'
import GetCurrentAddress from '../plugin/UserCountry'
import Swal from 'sweetalert2'

const Toast = Swal.mixin({
  toast:true,
  position:'top',
  showConfirmButton:false,
  timer:1500,
  timerProgressBar:true


})

function ProductDetail() {
    const [product, setProduct] = useState({})
    const [specifications, setSpecifications] = useState([])
    const [gallery, setGallery] = useState([])
    const [color, setColor] = useState([])
    const [size, setSize] = useState([])

    const [colorValue, setColorValue] = useState(['No Color'])
    const [sizeValue, setSizeValue] = useState(['No Size'])
    const [qtyValue, setQtyValue] = useState(1)

    const param = useParams()
    const userData = UserData()
    const currentAddress = GetCurrentAddress()
    const cart_id = CardID()


    useEffect(() => {
        apiInstance.get(`products/${param.slug}`).then((res) => {
            setProduct(res.data)
            setSpecifications(res.data.specification)
            setGallery(res.data.gallery)
            setColor(res.data.color)
            setSize(res.data.size)
        })
    }, [])
    
    const handleColorButtonClick = (event) => {
        const colorNameInput = event.target.closest('.color_button').parentNode.querySelector('.color_name')
        setColorValue(colorNameInput.value)
    }       

    const handleSizeButtonClick = (event) => {
        const sizeNameInput = event.target.closest('.size_button').parentNode.querySelector('.size_name')
        setSizeValue(sizeNameInput.value)
    }  
    
    const handleQtyChange = (event) => {
        setQtyValue(event.target.value)

    }

    const handleAddToCart = async () => {
       try {
        const formdata = new FormData()
        formdata.append('product_id', product.id)
        formdata.append('user_id', userData?.user_id)
        formdata.append('qty', qtyValue)
        formdata.append('price', product.price)
        formdata.append('shipping_amount', product.shipping_amount)
        formdata.append('country', currentAddress)
        formdata.append('size', sizeValue)
        formdata.append('color', colorValue)
        formdata.append('cart_id', cart_id)

        const response = await apiInstance.post('cart/', formdata)
        console.log(response.data)

        Toast.fire({
            icon: 'success',
            title: response.data.message
           })

       } catch (error) {
        console.log(error)
       }


    }

    return (
       
        <main className='mb-4 mt-4'>
            <div className='container'>
                {/* Section For Product Detail */}
                <section className='mb-5'>
                    <div className='row gx-lg-5'>
                        <div className='col-md-6 mb-4 mb-md-0'>
                            {/* Gallery */}
                            <div className=''>
                                <div className='row gx-2 gx-lg-3'>
                                    <div className='col-12 col-lg-12'>
                                        <div className='lightbox'>
                                            <img src={product.image}
                                                style={{
                                                    width: "100%",
                                                    height: 500,
                                                    objectFit: ConvolverNode,
                                                    borderRadius: 10
                                                }}
                                                alt='gallery image 1'
                                                className='ecommence-gallery-main-img active w-100 rounded-4'
                                            />
                                        </div>
                                    </div>                 
                                </div>
                                <div className='mt-3 d-flex'>
                                    {gallery.map((g, index) => (
                                        <div className='p-3' key={index}>
                                            <img src={g.image}
                                                style={{
                                                    width: 100,
                                                    height: 100,
                                                    objectFit: "cover",
                                                    boarderRadius: 10
                                                }}
                                                alt="Gallery image 1"
                                                className='ecommence-gallery-main-img active w-100 rounded-4'
                                            />

                                        </div>
                                    ))}

                                </div>
                                
                            </div>

                        </div>

                        <div className='col-md-6 mb-4 mb-md-0'>
                            {/* Detain */}
                            <div>
                                <h1 className='fw-bold mb-'>{product.title}</h1>
                                <div className='d-flex text-primary just align-items-center'>
                                    <ul className='mb-3 d-flex p-0' style={{ listStyle: 'none' }}>
                                        <li><i className='fas fa-star fa-sm text-warning ps-0' title='Bad' />
                                        </li>
                                        <li><i className='fas fa-star fa-sm text-warning ps-0' title='Bad' />
                                        </li>
                                        <li><i className='fas fa-star fa-sm text-warning ps-0' title='Bad' />
                                        </li>
                                        <li><i className='fas fa-star fa-sm text-warning ps-0' title='Bad' />
                                        </li>
                                        <li><i className='fas fa-star fa-sm text-warning ps-0' title='Bad' />
                                        </li>
                                        <li style={{ marginLeft: 10, fontSize: 13 }}>
                                            <a href='' className='text-decoration-none'>
                                                <strong className='me-'>4/5</strong>(2 reviews)
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                                <h5 className='mb-3'>
                                    <s className='text-muted me-2 small align-middle'>#{product.price}</s>
                                    <span className='align-middle'>#{product.price}</span>
                                </h5>
                                <p className='text-muted'>
                                    {product.description}
                                </p>
                                <div className='table-responsive'>
                                    <table className='table table-sm table-borderless mb-0'>
                                        <tbody>
                                            <tr>
                                                <th className='ps-0 w-25' scope='row'>
                                                    {" "}
                                                    <strong>Category</strong>
                                                </th>
                                                <td>{product.category?.title}</td>
                                            </tr>
                                            {specifications.map((s, index) => (
                                                <tr>
                                                <th className='ps-0 w-25' scope='row'>
                                                    <strong>{s.title}</strong>
                                                </th>
                                                <td>{s.content}</td>
                                                </tr>
                                            ))}
                                            
                                            
                                       
                                        </tbody>
                                    </table>

                                </div>
                            </div>
                            {/* Quantity */}
                            <div className='col-md-6 mb-4'>
                                <div className='form-outline'>
                                <label className='form-label' htmlFor="typeNumber">Quantity</label> 
                                    <input
                                        type='number'
                                        id='typeNumber'
                                        className='form-control'
                                        value={qtyValue}
                                        min={1}
                                        onChange={handleQtyChange}
                                    />
                                </div>

                            </div>
                            {/* Size */}
                            {size.length > 0 &&
                                <>
                                    <h6>Size: <span>{sizeValue}</span></h6>  
                                    <div className='col-md-6 mb-4'>
                                        <div className='d-flex'>
                                            {size?.map((s, index) => (
                                                <div>
                                                    <input  type='hidden' className='size_name' value={s.name}/>
                                                    <button className='btn btn-secondary m-1 size_button' type='button' onClick={handleSizeButtonClick} >{s.name}</button>
                                                </div>
                                            ))}
                                        </div>
                                    </div>
                                </>                            
                            }                            
                            {/* Color */}
                            {color.length > 0 &&
                                <>
                                    <h6>Color: <span>{colorValue}</span></h6>
                                    <div className='col-md-6 mb-4'>
                                        <div className='d-flex'>
                                            {color?.map((c, index) => (
                                                <div>
                                                    <input type='hidden' className='color_name' value={c.name} name='' id='' />
                                                    <button className='btn p-3 m-1 color_button' type='button' onClick={handleColorButtonClick} style={{backgroundColor: `${c.color_code}`}}>
                                                    </button>
                                                </div>
                                            ))}
                                        </div>
                                    </div>                                
                                </>                            
                            }
                            
                            <button type='button'
                                className='btn btn-primary btn-rounded me-2'
                                onClick={handleAddToCart}
                            >
                            <i className='fas fa-cart-plus me-2' />
                                Add to Cart
                            </button>
                        <button href="#!"
                            type='button'
                            className='btn btn-danger btn-floating'
                            data-mdb-toggle='tooltip'
                            title="Add to wishlist"
                        >
                            <i className='fas fa-heart' />
                        </button>

                        </div>
                        

                    </div>
                </section>

                {/* Section: Product details */}
                <hr />
                        <ul className="nav nav-pills mb-3" id="pills-tab" role="tablist">
                            <li className="nav-item" role="presentation">
                                <button
                                    className="nav-link active"
                                    id="pills-home-tab"
                                    data-bs-toggle="pill"
                                    data-bs-target="#pills-home"
                                    type="button"
                                    role="tab"
                                    aria-controls="pills-home"
                                    aria-selected="true"
                                >
                                    Specifications
                                </button>
                            </li>
                            <li className="nav-item" role="presentation">
                                <button
                                    className="nav-link"
                                    id="pills-profile-tab"
                                    data-bs-toggle="pill"
                                    data-bs-target="#pills-profile"
                                    type="button"
                                    role="tab"
                                    aria-controls="pills-profile"
                                    aria-selected="false"
                                >
                                    Vendor
                                </button>
                            </li>
                            <li className="nav-item" role="presentation">
                                <button
                                    className="nav-link"
                                    id="pills-contact-tab"
                                    data-bs-toggle="pill"
                                    data-bs-target="#pills-contact"
                                    type="button"
                                    role="tab"
                                    aria-controls="pills-contact"
                                    aria-selected="false"
                                >
                                    Review
                                </button>
                            </li>
                            <li className="nav-item" role="presentation">
                                <button
                                    className="nav-link"
                                    id="pills-disabled-tab"
                                    data-bs-toggle="pill"
                                    data-bs-target="#pills-disabled"
                                    type="button"
                                    role="tab"
                                    aria-controls="pills-disabled"
                                    aria-selected="false"
                                >
                                    Question &amp; Answer
                                </button>
                            </li>
                        </ul>
                        <div className="tab-content" id="pills-tabContent">
                            <div
                                className="tab-pane fade show active"
                                id="pills-home"
                                role="tabpanel"
                                aria-labelledby="pills-home-tab"
                                tabIndex={0}
                            >
                                <div className="table-responsive">
                                    <table className="table table-sm table-borderless mb-0">
                                        <tbody>
                                            {specifications?.map((s, index) => (
                                                <tr key={index}>
                                                    <th className="ps-0 w-25" scope="row"><strong>{s.title}</strong></th>
                                                    <td>{s.content}</td>
                                                </tr>
                                            ))}

                                        </tbody>
                                    </table>
                                </div>
                            </div>
                            </div>
            </div>
        
        </main>
      
        
    )
}

export default ProductDetail