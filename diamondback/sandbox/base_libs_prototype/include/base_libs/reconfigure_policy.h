/***************************************************************************
 *  include/base_libs/reconfigure_policy.h
 *  --------------------
 * 
 *  Copyright (c) 2011, Edward T. Kaszubski ( ekaszubski@gmail.com )
 *  All rights reserved.
 * 
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions are
 *  met:
 *  
 *  * Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *  * Redistributions in binary form must reproduce the above
 *    copyright notice, this list of conditions and the following disclaimer
 *    in the documentation and/or other materials provided with the
 *    distribution.
 *  * Neither the name of seabee3-ros-pkg nor the names of its
 *    contributors may be used to endorse or promote products derived from
 *    this software without specific prior written permission.
 *  
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 *  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 *  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 *  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 *  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 *  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 *  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 *  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 *  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 *  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 *  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 * 
 **************************************************************************/

#ifndef BASE_LIBS_BASE_LIBS_RECONFIGURE_POLICY_H_
#define BASE_LIBS_BASE_LIBS_RECONFIGURE_POLICY_H_

#include <base_libs/node_handle_policy.h>
#include <base_libs/auto_bind.h>
#include <dynamic_reconfigure/server.h>

namespace base_libs
{

BASE_LIBS_DECLARE_POLICY( Reconfigure, NodeHandlePolicy )

template<class __ReconfigureType>
BASE_LIBS_DECLARE_POLICY_CLASS( Reconfigure )
{
	BASE_LIBS_MAKE_POLICY_NAME( Reconfigure )
	
public:
	typedef __ReconfigureType _ReconfigureType;
	typedef dynamic_reconfigure::Server<__ReconfigureType> _ReconfigureServer;
	typedef ReconfigurePolicy<__ReconfigureType> _ReconfigurePolicy;
	
protected:
	__ReconfigureType config_;

private:
	_ReconfigureServer * server_;
	typename _ReconfigureServer::CallbackType external_callback_;
	
public:
	BASE_LIBS_DECLARE_POLICY_CONSTRUCTOR( Reconfigure ),
		server_( NULL )
	{
		printPolicyActionStart( "create", this );
		printPolicyActionDone( "create", this );
	}
	
	BASE_LIBS_ENABLE_INIT
	{
		printPolicyActionStart( "initialize", this );
		
		server_ = new _ReconfigureServer(
			ros::NodeHandle(
				NodeHandlePolicy::nh_rel_,
				ros::ParamReader<std::string, 1>::readParam( 
					NodeHandlePolicy::nh_rel_,
					getMetaParamDef<std::string>( "reconfigure_namespace_name", "reconfigure_namespace", args... ),
					"reconfigure" ) ) );
		
		server_->setCallback( base_libs::auto_bind( &_ReconfigurePolicy::reconfigureCB_0, this ) );
		
		printPolicyActionDone( "initialize", this );
	}
	
	~ReconfigurePolicy()
	{
		if( server_ ) delete server_;
	}
	
	void registerCallback( typename _ReconfigureServer::CallbackType external_callback )
	{
		external_callback_ = external_callback;
	}
	
private:
	void reconfigureCB_0( __ReconfigureType & config, uint32_t level )
	{
		config_ = config;
		if( external_callback_ ) external_callback_( config, level );
	}

/*
protected:
	void reconfigureCB( __ReconfigureType & config, uint32_t level )
	{
		//
	}*/
};

}

#endif // BASE_LIBS_BASE_LIBS_RECONFIGURE_POLICY_H_
