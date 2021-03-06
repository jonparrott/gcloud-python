# -*- coding: utf-8 -*-
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import google.api_core.grpc_helpers

from google.cloud.dlp_v2.proto import dlp_pb2_grpc


class DlpServiceGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.privacy.dlp.v2 DlpService API.

    The transport provides access to the raw gRPC stubs,
    which can be used to take advantage of advanced
    features of gRPC.
    """
    # The scopes needed to make gRPC calls to all of the methods defined
    # in this service.
    _OAUTH_SCOPES = ('https://www.googleapis.com/auth/cloud-platform', )

    def __init__(self,
                 channel=None,
                 credentials=None,
                 address='dlp.googleapis.com:443'):
        """Instantiate the transport class.

        Args:
            channel (grpc.Channel): A ``Channel`` instance through
                which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            address (str): The address where the service is hosted.
        """
        # If both `channel` and `credentials` are specified, raise an
        # exception (channels come with credentials baked in already).
        if channel is not None and credentials is not None:
            raise ValueError(
                'The `channel` and `credentials` arguments are mutually '
                'exclusive.', )

        # Create the channel.
        if channel is None:
            channel = self.create_channel(
                address=address,
                credentials=credentials,
            )

        self._channel = channel

        # gRPC uses objects called "stubs" that are bound to the
        # channel and provide a basic method for each RPC.
        self._stubs = {
            'dlp_service_stub': dlp_pb2_grpc.DlpServiceStub(channel),
        }

    @classmethod
    def create_channel(cls, address='dlp.googleapis.com:443',
                       credentials=None):
        """Create and return a gRPC channel object.

        Args:
            address (str): The host for the channel to use.
            credentials (~.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return google.api_core.grpc_helpers.create_channel(
            address,
            credentials=credentials,
            scopes=cls._OAUTH_SCOPES,
        )

    @property
    def channel(self):
        """The gRPC channel used by the transport.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return self._channel

    @property
    def inspect_content(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Finds potentially sensitive info in content.
        This method has limits on input size, processing time, and output size.

        When no InfoTypes or CustomInfoTypes are specified in this request, the
        system will automatically choose what detectors to run. By default this may
        be all types, but may change over time as detectors are updated.

        For how to guides, see https://cloud.google.com/dlp/docs/inspecting-images
        and https://cloud.google.com/dlp/docs/inspecting-text,

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].InspectContent

    @property
    def redact_image(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Redacts potentially sensitive info from an image.
        This method has limits on input size, processing time, and output size.
        See https://cloud.google.com/dlp/docs/redacting-sensitive-data-images to
        learn more.

        When no InfoTypes or CustomInfoTypes are specified in this request, the
        system will automatically choose what detectors to run. By default this may
        be all types, but may change over time as detectors are updated.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].RedactImage

    @property
    def deidentify_content(self):
        """Return the gRPC stub for {$apiMethod.name}.

        De-identifies potentially sensitive info from a ContentItem.
        This method has limits on input size and output size.
        See https://cloud.google.com/dlp/docs/deidentify-sensitive-data to
        learn more.

        When no InfoTypes or CustomInfoTypes are specified in this request, the
        system will automatically choose what detectors to run. By default this may
        be all types, but may change over time as detectors are updated.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].DeidentifyContent

    @property
    def reidentify_content(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Re-identifies content that has been de-identified. See
        https://cloud.google.com/dlp/docs/pseudonymization#re-identification\_in\_free\_text\_code\_example
        to learn more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].ReidentifyContent

    @property
    def list_info_types(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Returns a list of the sensitive information types that the DLP API
        supports. See https://cloud.google.com/dlp/docs/infotypes-reference to
        learn more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].ListInfoTypes

    @property
    def create_inspect_template(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Creates an InspectTemplate for re-using frequently used configuration
        for inspecting content, images, and storage.
        See https://cloud.google.com/dlp/docs/creating-templates to learn more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].CreateInspectTemplate

    @property
    def update_inspect_template(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Updates the InspectTemplate.
        See https://cloud.google.com/dlp/docs/creating-templates to learn more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].UpdateInspectTemplate

    @property
    def get_inspect_template(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Gets an InspectTemplate.
        See https://cloud.google.com/dlp/docs/creating-templates to learn more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].GetInspectTemplate

    @property
    def list_inspect_templates(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Lists InspectTemplates.
        See https://cloud.google.com/dlp/docs/creating-templates to learn more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].ListInspectTemplates

    @property
    def delete_inspect_template(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Deletes an InspectTemplate.
        See https://cloud.google.com/dlp/docs/creating-templates to learn more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].DeleteInspectTemplate

    @property
    def create_deidentify_template(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Creates a DeidentifyTemplate for re-using frequently used configuration
        for de-identifying content, images, and storage.
        See https://cloud.google.com/dlp/docs/creating-templates-deid to learn
        more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].CreateDeidentifyTemplate

    @property
    def update_deidentify_template(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Updates the DeidentifyTemplate.
        See https://cloud.google.com/dlp/docs/creating-templates-deid to learn
        more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].UpdateDeidentifyTemplate

    @property
    def get_deidentify_template(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Gets a DeidentifyTemplate.
        See https://cloud.google.com/dlp/docs/creating-templates-deid to learn
        more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].GetDeidentifyTemplate

    @property
    def list_deidentify_templates(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Lists DeidentifyTemplates.
        See https://cloud.google.com/dlp/docs/creating-templates-deid to learn
        more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].ListDeidentifyTemplates

    @property
    def delete_deidentify_template(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Deletes a DeidentifyTemplate.
        See https://cloud.google.com/dlp/docs/creating-templates-deid to learn
        more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].DeleteDeidentifyTemplate

    @property
    def create_dlp_job(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Creates a new job to inspect storage or calculate risk metrics.
        See https://cloud.google.com/dlp/docs/inspecting-storage and
        https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more.

        When no InfoTypes or CustomInfoTypes are specified in inspect jobs, the
        system will automatically choose what detectors to run. By default this may
        be all types, but may change over time as detectors are updated.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].CreateDlpJob

    @property
    def list_dlp_jobs(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Lists DlpJobs that match the specified filter in the request.
        See https://cloud.google.com/dlp/docs/inspecting-storage and
        https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].ListDlpJobs

    @property
    def get_dlp_job(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Gets the latest state of a long-running DlpJob.
        See https://cloud.google.com/dlp/docs/inspecting-storage and
        https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].GetDlpJob

    @property
    def delete_dlp_job(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Deletes a long-running DlpJob. This method indicates that the client is
        no longer interested in the DlpJob result. The job will be cancelled if
        possible.
        See https://cloud.google.com/dlp/docs/inspecting-storage and
        https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].DeleteDlpJob

    @property
    def cancel_dlp_job(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Starts asynchronous cancellation on a long-running DlpJob. The server
        makes a best effort to cancel the DlpJob, but success is not
        guaranteed.
        See https://cloud.google.com/dlp/docs/inspecting-storage and
        https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].CancelDlpJob

    @property
    def list_job_triggers(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Lists job triggers.
        See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].ListJobTriggers

    @property
    def get_job_trigger(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Gets a job trigger.
        See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].GetJobTrigger

    @property
    def delete_job_trigger(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Deletes a job trigger.
        See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].DeleteJobTrigger

    @property
    def update_job_trigger(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Updates a job trigger.
        See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].UpdateJobTrigger

    @property
    def create_job_trigger(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Creates a job trigger to run DLP actions such as scanning storage for
        sensitive information on a set schedule.
        See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].CreateJobTrigger

    @property
    def create_stored_info_type(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Creates a pre-built stored infoType to be used for inspection.
        See https://cloud.google.com/dlp/docs/creating-stored-infotypes to
        learn more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].CreateStoredInfoType

    @property
    def update_stored_info_type(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Updates the stored infoType by creating a new version. The existing version
        will continue to be used until the new version is ready.
        See https://cloud.google.com/dlp/docs/creating-stored-infotypes to
        learn more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].UpdateStoredInfoType

    @property
    def get_stored_info_type(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Gets a stored infoType.
        See https://cloud.google.com/dlp/docs/creating-stored-infotypes to
        learn more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].GetStoredInfoType

    @property
    def list_stored_info_types(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Lists stored infoTypes.
        See https://cloud.google.com/dlp/docs/creating-stored-infotypes to
        learn more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].ListStoredInfoTypes

    @property
    def delete_stored_info_type(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Deletes a stored infoType.
        See https://cloud.google.com/dlp/docs/creating-stored-infotypes to
        learn more.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['dlp_service_stub'].DeleteStoredInfoType
