/***************************************************************************
 *  include/seabee3_teleop/seabee3_teleop.h
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

#ifndef SEABEE3_TELEOP_SEABEE3_TELEOP_SEABEE3_TELEOP_H_
#define SEABEE3_TELEOP_SEABEE3_TELEOP_SEABEE3_TELEOP_H_

#include <base_libs/node.h>
#include <base_libs/joystick_policy.h>
#include <base_libs/service_client_policy.h>
#include <seabee3_driver/FiringDeviceAction.h>

typedef base_libs::JoystickPolicy _JoystickPolicy;
typedef seabee3_driver::FiringDeviceAction _FiringDeviceActionService;
typedef base_libs::ServiceClientPolicy<_FiringDeviceActionService, 0> _ServiceClientPolicy1;
typedef base_libs::ServiceClientPolicy<_FiringDeviceActionService, 1> _ServiceClientPolicy2;
typedef base_libs::ServiceClientPolicy<_FiringDeviceActionService, 2> _ServiceClientPolicy3;
typedef base_libs::ServiceClientPolicy<_FiringDeviceActionService, 3> _ServiceClientPolicy4;

BASE_LIBS_DECLARE_NODE( Seabee3Teleop, _JoystickPolicy, _ServiceClientPolicy1, _ServiceClientPolicy2, _ServiceClientPolicy3, _ServiceClientPolicy4 )

BASE_LIBS_DECLARE_NODE_CLASS( Seabee3Teleop )
{
public:
	int current_firing_device_;
	int num_firing_devices_;
	_JoystickPolicy::_Axis::_Name current_button_;
	
	BASE_LIBS_DECLARE_NODE_CONSTRUCTOR( Seabee3Teleop ),
		current_firing_device_( 0 ),
		num_firing_devices_( 4 ),
		current_button_( "" )
	{
		//
	}
	
	bool tryGetButtonLock( const _JoystickPolicy::_Axis & axis, const _JoystickPolicy::_JoystickMsg::ConstPtr & msg )
	{
		if( axis.getValueAsButton( msg ) > 0 )
		{
			if( current_button_ == "" )
			{
				//PRINT_INFO( "Axis [ %s ] gained lock", axis.name_.c_str() );
				
				current_button_ = axis.name_;
				return true;
			}
		}
		else
		{
			if( current_button_ == axis.name_ )
			{
				//PRINT_INFO( "Axis [ %s ] released lock", axis.name_.c_str() );
				current_button_ = "";
			}
		}
		
		return false;
	}
	
	BASE_LIBS_DECLARE_MESSAGE_CALLBACK( joystickCB, _JoystickPolicy::_JoystickMsg )
	{
		if( JoystickPolicy::isEnabled() )
		{
			const auto & next_firing_device_axis = _JoystickPolicy::getAxis( "next_firing_device" );
			const auto & prev_firing_device_axis = _JoystickPolicy::getAxis( "prev_firing_device" );
			const auto & fire_device_axis = _JoystickPolicy::getAxis( "fire_device" );
			
			if( tryGetButtonLock( next_firing_device_axis, msg ) ) ++current_firing_device_;
			if( tryGetButtonLock( prev_firing_device_axis, msg ) ) --current_firing_device_;
			
			if( num_firing_devices_ > 0 )
			{
				if( current_firing_device_ > num_firing_devices_ - 1 ) current_firing_device_ = 0;
				if( current_firing_device_ < 0 ) current_firing_device_ = num_firing_devices_ - 1;
			}
			
			if( tryGetButtonLock( fire_device_axis, msg ) ) fireCurrentDevice();
		}
	}
	
	void fireCurrentDevice()
	{
		PRINT_INFO( "Firing current device: %i", current_firing_device_ );
		
		_FiringDeviceActionService service;
		
		switch( current_firing_device_ )
		{
		case 0:
			_ServiceClientPolicy1::callService( service );
			break;
		case 1:
			_ServiceClientPolicy2::callService( service );
			break;
		case 2:
			_ServiceClientPolicy3::callService( service );
			break;
		case 3:
			_ServiceClientPolicy4::callService( service );
			break;
		}
	}
	
	void spinFirst()
	{
		auto nh_rel = base_libs::RunablePolicy::getNodeHandle();
		
		nh_rel.setParam( "shooter1_service_name", "/seabee3/shooter1" );
		_ServiceClientPolicy1::init( "service_name_param", std::string( "shooter1_service_name" ) );
		
		nh_rel.setParam( "shooter2_service_name", "/seabee3/shooter2" );
		_ServiceClientPolicy2::init( "service_name_param", std::string( "shooter2_service_name" ) );
		
		nh_rel.setParam( "dropper1_service_name", "/seabee3/dropper1" );
		_ServiceClientPolicy3::init( "service_name_param", std::string( "dropper1_service_name" ) );
		
		nh_rel.setParam( "dropper2_service_name", "/seabee3/dropper2" );
		_ServiceClientPolicy4::init( "service_name_param", std::string( "dropper2_service_name" ) );
		
	}
	
	void spinOnce()
	{
		_JoystickPolicy::update();
	}
};

#endif // SEABEE3_TELEOP_SEABEE3_TELEOP_SEABEE3_TELEOP_H_
