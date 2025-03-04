import React from 'react'

function Cart() {
  return (
    <div>
      <main className='mt-5'>
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
                      {/* Single item */}
                      <div className='row border-bottom mb-4'>
                        <div className='col-md-2 mb-4 mb-md-0'>
                          <div className='bg-image ripple rounded-5 mb-4 overflow-hidden d-block'
                            data-ripple-color='light'
                          >
                            <img
                              src='' 
                              className='w-100'
                              alt='big image'
                              style={{ height: "100px", objectFit: "cover", borderRadius: "10px" }}
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
                      </div>
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